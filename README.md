# Treasure Hunt Game 🎮💎

A fun and interactive treasure hunt game with hidden clues and codes!
Solve riddles, find codes, and unlock surprises! 🎉

This game is built with Python and Flet, fully customizable for any occasion. Clone, edit, and share the fun! 🚀

---

## How It Works

The game guides the player through a series of riddles and clues, each hidden behind a code that must be entered correctly to progress to the next stage. Here's how it works:

1. **Start the Game**: Players are welcomed with an introductory message.
2. **Clues & Codes**: Each stage presents a riddle, and players must input the correct code to continue.
3. **Input**: Players type the code they believe is correct.
4. **Completion**: Once all riddles are solved, players are congratulated, and the game ends.

---

## Features

- **Interactive Gameplay**: Players actively solve riddles and input codes.
- **Customizable Clues and Codes**: Easy to modify for any theme or occasion.
- **Simple Interface**: Built using the Flet library for easy setup and minimal dependencies.

---

## How to Run the Game

To run the game locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your_username/treasure-hunt-game.git
   cd treasure-hunt-game

2. **Install the Required Dependencies**:
Ensure you have Python installed, then run:
   ```python
   pip install flet
   
3. **Run the Game**:
Start the game with:
   ```bash
   python game.py
The game will open automatically.

## How to Modify the Game

This game is designed to be easily customizable. Here’s how you can make changes:

1. **Change the Riddles and Codes**:
Update the dictionary storing the clues and codes:
   ```python
   codes = {
    1: ("8341", "Clue text..."),
    2: ("9474", "Another clue..."),
    # Add more clues as needed
}

2. **Adjust Game Difficulty**:
You can make the game easier or harder by:

   Modifying the riddles.
   
   Setting simpler or more complex codes.
   
   Adding more stages to the game.

3. **Edit the Visuals**:
Customize the game’s appearance by modifying the layout in the code:
   ```python
   label_position = ft.Text(f"Clue {position}", size=30, weight=ft.FontWeight.BOLD)
   label_charade = ft.Text("Clue text...", size=20, color="blue")

4. **Add More Stages**:

   Expand the codes dictionary with additional clues and codes. Ensure the game logic supports these new stages.

## Contributing

We welcome contributions! If you have ideas for new features, improvements, or bug fixes, feel free to fork the repository and submit a pull request.
