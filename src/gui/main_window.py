import tkinter as tk
from src.gui.game_view import GameView
from src.gui.controllers import GUIController
from src.game.game_controller import GameController
from src.players.human_player import HumanPlayer

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AlphaQuarto")
        
        window_width = 1000
        window_height = 800

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.configure(bg='#333')

        self._current_view = None
        self._main_menu_frame = None  # Keep a reference to the main menu
        self._setup_main_menu()

        self.lift()
        self.attributes('-topmost', True)
        self.after_idle(self.attributes, '-topmost', False)
        self.focus_force()

    def _clear_view(self):
        """Destroys the current view."""
        if self._current_view:
            self._current_view.destroy()
            self._current_view = None
        if self._main_menu_frame:
            self._main_menu_frame.destroy()
            self._main_menu_frame = None

    def _setup_main_menu(self):
        """Sets up the initial menu."""
        self._clear_view()

        self._main_menu_frame = tk.Frame(self, bg='#333')
        self._main_menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        welcome_label = tk.Label(self._main_menu_frame, text="Welcome to AlphaQuarto", font=("Helvetica", 24, "bold"), fg='white', bg='#333')
        welcome_label.pack(pady=20)

        game_button = tk.Button(self._main_menu_frame, text="Start Human vs. Human Game", command=self._on_game_button_click, font=("Helvetica", 14), width=30)
        game_button.pack(pady=20, ipady=10)

    def _on_game_button_click(self):
        """Callback function when the game button is clicked."""
        self._show_game_view()
    
    def _show_game_view(self):
        """Displays the game view and hides the main menu."""
        self._clear_view()

        # 1. Create Model and Player objects
        player1 = HumanPlayer("Player 1")
        player2 = HumanPlayer("Player 2")
        game_controller = GameController(player1, player2)

        # 2. Create View
        self._current_view = GameView(self)
        
        # 3. Create Controller to link them
        GUIController(game_controller, self._current_view)