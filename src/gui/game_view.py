import tkinter as tk
from tkinter import font

from src.utils.helpers import STATE_SELECT_PIECE, STATE_PLACE_PIECE, STATE_GAME_OVER

class GameView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='#333')
        self.controller = None
        self.pack(fill=tk.BOTH, expand=True)
        self._create_widgets()

    def set_controller(self, controller):
        self.controller = controller

    def _create_widgets(self):
        # Main layout frames
        self.status_frame = tk.Frame(self, bg='#444')
        self.status_frame.pack(side=tk.TOP, fill=tk.X, ipady=10)

        self.board_frame = tk.Frame(self, bg='#333')
        self.board_frame.pack(side=tk.LEFT, padx=50, pady=50, anchor='n')

        self.pieces_frame = tk.Frame(self, bg='#333')
        self.pieces_frame.pack(side=tk.RIGHT, padx=50, pady=50, anchor='n')

        # Status Label
        self.status_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.status_label = tk.Label(self.status_frame, text="Welcome to Quarto!", font=self.status_font, fg='white', bg='#444')
        self.status_label.pack(pady=5)

        # Board Canvas
        self.board_canvas = tk.Canvas(self.board_frame, width=400, height=400, bg='#555', highlightthickness=0)
        self.board_canvas.pack()
        self.board_canvas.bind("<Button-1>", self._on_board_click)
        self.cell_size = 100

        # Available Pieces Canvas
        tk.Label(self.pieces_frame, text="Available Pieces", font=("Helvetica", 14), fg='white', bg='#333').pack(pady=(0, 10))
        self.pieces_canvas = tk.Canvas(self.pieces_frame, width=220, height=440, bg='#555', highlightthickness=0)
        self.pieces_canvas.pack()
        self.pieces_canvas.bind("<Button-1>", self._on_piece_click)
        self.piece_cell_size = 55

        # Reset button
        self.reset_button = tk.Button(self.status_frame, text="Reset Game", command=self._on_reset_click)
        self.reset_button.pack(pady=5)

    def _on_board_click(self, event):
        if self.controller:
            col = event.x // self.cell_size
            row = event.y // self.cell_size
            if 0 <= row < 4 and 0 <= col < 4:
                self.controller.handle_board_click(row, col)

    def _on_piece_click(self, event):
        if self.controller:
            col = event.x // self.piece_cell_size
            row = event.y // self.piece_cell_size
            if 0 <= col < 4 and 0 <= row < 4:
                piece_id = row * 4 + col
                self.controller.handle_piece_click(piece_id)

    def _on_reset_click(self):
        if self.controller:
            self.controller.handle_reset_click()

    def draw_board(self, board):
        self.board_canvas.delete("all")
        for r in range(4):
            for c in range(4):
                x1, y1 = c * self.cell_size, r * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                self.board_canvas.create_rectangle(x1, y1, x2, y2, outline='#ccc', fill='#777')
                
                piece = board.get_piece(r, c)
                if piece:
                    self._draw_piece(self.board_canvas, x1, y1, self.cell_size, piece)

    def draw_available_pieces(self, available_pieces, all_pieces):
        self.pieces_canvas.delete("all")
        for i in range(16):
            row, col = divmod(i, 4)
            x1 = col * self.piece_cell_size
            y1 = row * self.piece_cell_size
            
            # Draw empty slot background
            self.pieces_canvas.create_rectangle(
                x1, y1, x1 + self.piece_cell_size, y1 + self.piece_cell_size,
                outline='#888', fill='#666'
            )

            if i in available_pieces:
                piece = all_pieces[i]
                self._draw_piece(self.pieces_canvas, x1, y1, self.piece_cell_size, piece)

    def _draw_piece(self, canvas, x, y, size, piece):
        padding = size * 0.15
        x1, y1 = x + padding, y + padding
        x2, y2 = x + size - padding, y + size - padding

        # Color
        fill_color = '#d18b47' if piece.is_dark else '#ffdead' # Dark wood vs Light wood

        # Shape
        if piece.is_square:
            canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline=fill_color)
        else: # Circle
            canvas.create_oval(x1, y1, x2, y2, fill=fill_color, outline=fill_color)

        # Height (inner marking)
        if not piece.is_tall:
            h_pad = size * 0.1
            canvas.create_line(x1+h_pad, y1+h_pad, x2-h_pad, y1+h_pad, width=2, fill='black')

        # Top (solid/hollow)
        if not piece.is_solid:
            s_pad = size * 0.3
            canvas.create_oval(x+s_pad, y+s_pad, x+size-s_pad, y+size-s_pad, fill='#333' if not piece.is_square else fill_color, outline='black', width=2)


    def update_status_message(self, state, current_player, piece_to_place, winner):
        msg = ""
        if state == STATE_GAME_OVER:
            if winner:
                msg = f"GAME OVER! {winner.name} wins!"
            else:
                msg = "GAME OVER! It's a draw."
            # Highlight winning line would be a great addition here
        elif state == STATE_SELECT_PIECE:
            msg = f"{current_player.name}, please SELECT a piece for your opponent."
        elif state == STATE_PLACE_PIECE:
            piece_desc = f"{'Tall' if piece_to_place.is_tall else 'Short'}, {'Dark' if piece_to_place.is_dark else 'Light'}, {'Square' if piece_to_place.is_square else 'Circle'}, {'Solid' if piece_to_place.is_solid else 'Hollow'}"
            self.status_label.config(font=(self.status_font.cget("family"), 12)) # Smaller font for long text
            msg = f"{current_player.name}, please PLACE this piece on the board."
        
        self.status_label.config(text=msg)
        if state != STATE_PLACE_PIECE:
             self.status_label.config(font=self.status_font)