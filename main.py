import sys
import os
import tkinter as tk # Import tkinter here, as the main app runs it

# Add the 'src' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import your main window, game manager, and agent trainer
from src.gui.main_window import MainWindow
from src.game.manager import GameManager
from src.agent.train_agent import AgentTrainer

def main():
    # Initialize your core logic components
    game_manager = GameManager()
    agent_trainer = AgentTrainer()

    # Pass these instances to your MainWindow
    # This allows the GUI to interact with your game and agent logic
    app = MainWindow(game_manager=game_manager, agent_trainer=agent_trainer)
    app.mainloop() # Start the Tkinter event loop

if __name__ == "__main__":
    main()