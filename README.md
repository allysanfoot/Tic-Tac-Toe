# Tic-Tac-Toe Game

## Overview
This is a simple text-based implementation of the classic Tic-Tac-Toe game. The game is played between two players who take turns to place their markers (`X` or `O`) on a 3x3 grid. The objective is to get three of your markers in a row, either horizontally, vertically, or diagonally.

## Features
- **Two-Player Mode**: Play against a friend.
- **Choose Marker**: Player 1 can choose `X` or `O`.
- **Random First Player**: The game randomly selects which player goes first.
- **Validation**: Ensures valid moves and prevents overwriting of markers.
- **Replay Option**: Players can choose to play again after a match ends.

## How to Play
- The board has 9 positions:
1 | 2 | 3
4 | 5 | 6
7 | 9 | 9

- Players take turns to place their marker (`X` or `O`) on an empty position.
- The game ends when a player successfully places three markers in a row or when all positions are filled without a winner.

## Setup Instructions

1. **Clone the Repository**
  ```sh
  git clone https://github.com/your-username/tic-tac-toe.git
  cd tic-tac-toe
  ```

2. **Run the Game**
  - The game runs in Python. Make sure you have Python installed.
  ```sh
  python tic_tac_toe.py
  ```

## Functions Explained

- **`display_board(board)`**: Displays the current state of the board.
- **`player_input()`**: Allows Player 1 to choose a marker (`X` or `O`), and assigns the other marker to Player 2.
- **`place_marker(board, marker, position)`**: Places the player's marker at the chosen position.
- **`win_check(board, mark)`**: Checks if a player has won.
- **`choose_first()`**: Randomly selects which player goes first.
- **`space_check(board, position)`**: Checks if a position on the board is available.
- **`full_board_check(board)`**: Checks if the board is full.
- **`player_choice(board)`**: Allows the current player to choose a position for their move.
- **`replay()`**: Asks the players if they want to play again after the game ends.

## Example Gameplay
1. Player 1 is prompted to choose their marker (`X` or `O`).
2. The game randomly selects which player goes first.
3. Players take turns to enter their move, which is validated for correctness.
4. The game ends with a win or draw, and players are asked if they want to replay.

## Directory Structure
```
tic-tac-toe/
├── tic_tac_toe.py       # Main game script
├── __pycache__/         # Compiled Python files
└── README.md            # Project documentation
```

## Contributing
Feel free to fork this repository, submit issues, or contribute by making a pull request. Any contributions are greatly appreciated!

## License
This project is open source and available under the [MIT License](LICENSE).

