import tkinter as tk
from tkinter import Menu, messagebox

class MainWindow(tk.Tk):
    def __init__(self, game_manager=None, agent_trainer=None):
        """
        Initializes the main application window.

        Args:
            game_manager: An instance of a class that manages game logic (e.g., from src.game).
            agent_trainer: An instance of a class that handles agent training (e.g., from src.agent.train_agent).
        """
        super().__init__()
        self.title("Quarto AI")
        self.geometry("800x600") # Set a default size for the window

        # Store references to managers if passed
        self.game_manager = game_manager
        self.agent_trainer = agent_trainer

        self._create_menu_bar()
        self._create_main_layout()

    def _create_menu_bar(self):
        """
        Creates the main menu bar for the application.
        """
        menubar = Menu(self)
        self.config(menu=menubar)

        # --- Game Menu ---
        game_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="New Human vs. Human Game", command=self._start_human_vs_human_game)
        game_menu.add_command(label="New Human vs. AI Game", command=self._start_human_vs_ai_game)
        game_menu.add_command(label="New AI vs. AI Game", command=self._start_ai_vs_ai_game)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.quit)

        # --- Agent Menu ---
        agent_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Agent", menu=agent_menu)
        agent_menu.add_command(label="Train AlphaQuarto Agent", command=self._train_alpha_quarto_agent)
        agent_menu.add_command(label="Load Trained Agent", command=self._load_trained_agent)
        agent_menu.add_command(label="Save Current Agent", command=self._save_current_agent) # Implement save later

        # --- Help Menu ---
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self._show_about_dialog)

    def _create_main_layout(self):
        """
        Creates the main layout of the window where game view and controls will go.
        """
        # This is a placeholder. You'll replace this with your actual game board
        # and control widgets from game_view.py and other UI elements.
        self.main_frame = tk.Frame(self, bg="white")
        self.main_frame.pack(expand=True, fill="both", padx=10, pady=10)

        welcome_label = tk.Label(self.main_frame, text="Welcome to Quarto AI!", font=("Arial", 24), bg="black")
        welcome_label.pack(pady=50)

        instruction_label = tk.Label(self.main_frame, text="Use the 'Game' menu to start a new game.", font=("Arial", 14), bg="black")
        instruction_label.pack(pady=20)


    # --- Menu Command Callbacks ---
    def _start_human_vs_human_game(self):
        """Starts a new human vs. human game."""
        messagebox.showinfo("Game Mode", "Starting new Human vs. Human game...")
        # Placeholder: Call self.game_manager.start_game(player1_type="human", player2_type="human")
        # Then update your game_view to display the board.

    def _start_human_vs_ai_game(self):
        """Starts a new human vs. AI game."""
        messagebox.showinfo("Game Mode", "Starting new Human vs. AI game...")
        # Placeholder: Call self.game_manager.start_game(player1_type="human", player2_type="ai")

    def _start_ai_vs_ai_game(self):
        """Starts a new AI vs. AI game."""
        messagebox.showinfo("Game Mode", "Starting new AI vs. AI game...")
        # Placeholder: Call self.game_manager.start_game(player1_type="ai", player2_type="ai")

    def _train_alpha_quarto_agent(self):
        """Initiates the Q-learning agent training process."""
        messagebox.showinfo("Agent Training", "Starting AlphaQuarto agent training... (Check console for progress)")
        # Placeholder: Call self.agent_trainer.train() if agent_trainer is provided
        if self.agent_trainer:
            # You might want to run this in a separate thread to keep the GUI responsive
            # For simplicity, we'll just call it directly for now.
            # In a real app, use threading or async.
            self.agent_trainer.train_agent()
            messagebox.showinfo("Agent Training", "AlphaQuarto agent training completed!")
        else:
            messagebox.showerror("Error", "Agent trainer not initialized!")


    def _load_trained_agent(self):
        """Loads a pre-trained agent model."""
        messagebox.showinfo("Agent Management", "Loading trained agent...")
        # Placeholder: Implement file dialog to select model, then load via agent_trainer

    def _save_current_agent(self):
        """Saves the current state of the agent model."""
        messagebox.showinfo("Agent Management", "Saving current agent...")
        # Placeholder: Implement save dialog to choose location, then save via agent_trainer

    def _show_about_dialog(self):
        """Displays an about dialog."""
        messagebox.showinfo(
            "About Quarto AI",
            "Quarto AI Project\n\nDeveloped by [Your Name/Team Name]\nVersion 1.0\n\nAn AI agent learning to master the game of Quarto using Q-learning."
        )

# This part is crucial for main.py to run the GUI
if __name__ == "__main__":
    # When testing main_window.py directly, you can run it like this:
    # However, in your actual project, main.py will be the entry point.
    app = MainWindow()
    app.mainloop()