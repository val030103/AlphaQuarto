This is a personal project dedicated to create an AI agent
that play the game Quarto using reinforcement learning, specifically Q-learning.

## Quarto Game Rules
Quarto is a two-player abstract strategy game invented by Blaise Müller. It's renowned for its unique piece-selection mechanic and its blend of simple rules with deep strategic complexity.

### 1. Game Components
Game Board: A 4x4 grid (16 squares).

Pieces: There are 16 unique game pieces. Each piece possesses four distinct characteristics, and for each characteristic, there are two possible states (binary attributes):

Height: Tall or Short
Color: Light or Dark (often natural wood vs. stained wood)
Shape: Square or Round
Hollowness: Hollow-top or Solid-top
Since each piece has four binary attributes, there are 16 unique combinations, meaning every piece is distinct from all others.

### 2. Objective of the Game
The goal of Quarto is to be the first player to place a piece on the board that completes a line of four pieces (horizontally, vertically, or diagonally) or a 2x2 square where all four pieces in that line or square share at least one common characteristic.

Examples of Winning Lines:

Four Tall pieces in a row (horizontal, vertical, or diagonal).
Four Round pieces in a 2x2 square.
Four Light pieces in a row.
Four Hollow-top pieces in a 2x2 square.
And so on for any of the eight attributes.

It does not matter if the pieces share other characteristics; as long as they share at least one common characteristic, it's a win.

### 3. Game Setup

Place all 16 unique pieces off to the side of the board, within view of both players. The board starts empty.
Players decide who goes first (e.g., by flipping a coin or mutual agreement).

### 4. How to Play (Turns)
Quarto has a unique turn structure: The player whose turn it is does NOT choose the piece they will place. Instead, they choose a piece from the available unplayed pieces and give it to their opponent to place.

A turn consists of two actions:

Place the Piece: The current player receives a piece from their opponent (or selects the first piece if it's the very first turn of the game). They must place this piece onto any empty square on the 4x4 board. Once placed, a piece cannot be moved.
Choose the Next Piece: After placing the piece, the current player must then choose one of the remaining unplayed pieces and give it to their opponent. This piece will be placed by the opponent on their next turn.
This sequence continues back and forth until a player wins or all pieces are placed.

First Turn Exception:

The player who starts the game (Player 1) does not place a piece in their first action. Instead, they simply choose one of the 16 pieces and give it to Player 2.
Player 2 then places that piece, and then chooses one of the remaining 15 pieces to give back to Player 1.
From that point on, turns follow the "Place Piece, then Choose Piece" sequence described above.

### 5. Winning the Game
A player wins the game by placing a piece that completes a line or square of four pieces (horizontal, vertical, or diagonal) all sharing at least one common characteristic.

If a player places a winning piece and immediately declares so: They win the game.
If a player places a winning piece but fails to declare it: The game continues. If the opponent notices the overlooked winning line before making their own move (i.e., before placing the piece they were given), they can declare quarto and claim the win.
If neither player notices a winning line during the turn it was created, and moves continue: That winning line loses its value, and the game continues until another Quarto is formed and declared, or the game ends in a draw.

### 6. End of the Game
Win: The game ends immediately when a player successfully declares quarto
Draw: If all 16 pieces are placed on the board and no player has managed to form a Quarto and declare it, the game ends in a draw.

### 7. Strategic Nuances
The unique piece-selection rule is what makes Quarto so strategic. You must:

Think ahead: Consider not only where you want to place a piece, but also which piece you are forcing your opponent to play.
Set traps: Try to create situations where any piece your opponent is forced to play will lead to a win for you.
Avoid traps: Be mindful that the piece you give to your opponent might create a winning opportunity for them.
Understand attributes: Constantly keep track of which attributes are shared across lines and squares, and which pieces (with which attributes) are still available.




## Current folder structure

ALPHAQUARTO/
├── src/
│   ├── game/
│   │   ├── __init__.py
│   │   ├── board.py          # Defines the Quarto board state, placing pieces, checking for wins
│   │   ├── piece.py          # Defines the Quarto pieces and their attributes
│   │   └── rules.py          # Implements game rules, win conditions, valid moves
│   ├── players/
│   │   ├── __init__.py
│   │   ├── human_player.py   # Logic for human input (adapt to GUI events)
│   │   └── base_player.py    # Abstract base class for players if needed
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── q_learner.py      # Implements the Q-learning algorithm, Q-table/network, update rules
│   │   ├── agent_player.py   # Wrapper for the Q-learning agent to interact with the game
│   │   ├── train_agent.py    # Script dedicated to training the Q-learning agent
│   │   └── models/           # Folder to save trained Q-tables or neural networks
│   │       └── q_table.pkl   # Example: Saved Q-table
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main_window.py    # Defines the main GUI window, layout, and event handling
│   │   ├── game_view.py      # Handles drawing the Quarto board and pieces
│   │   └── controllers.py    # Logic to connect GUI events to game/agent actions
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py        # General utility functions (e.g., state serialization, constants)
├── main.py                   # Main entry point to launch the GUI application
├── README.md                 # Project description, how to run, etc.
└── .gitignore                # Files/folders to ignore in Git