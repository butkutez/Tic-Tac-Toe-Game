# Tic-Tac-Toe Game
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Property_Price_Predictor](https://w0.peakpx.com/wallpaper/711/59/HD-wallpaper-tic-tac-toe-game-background-ultra-games-other-games-game-design-background-tictactoe-chalkboard-chalk-diagonal-row-winner-grid-greenish-turquoise.jpg)](https://www.peakpx.com/en/hd-wallpaper-desktop-agtqi)  
*Image source: [Peakpx](https://www.peakpx.com/en/hd-wallpaper-desktop-agtqi)*

## Project Description

This is a classic Tic-Tac-Toe game created using the Python programming language. It is a two-player game played on a 3x3 grid where players alternate placing their symbol (X or O). The goal is to align three of your symbols horizontally, vertically, or diagonally. The game ends in a draw if the board fills up without a winner.

## Core Implementation
This project utilizes several fundamental programming concepts:
- Functions
- Loops
- Conditionals
- Input validation
- Basic game logic

## Getting started

### Installation
You need to have Python 3.x installed on your system.

**1. Clone the project**

```
cmd git clone https://github.com/butkutez/Tic-Tac-Toe-Game.git
```
**2. Navigate to the project folder**
```
cd Tic-Tac-Toe-Game
```

**3. Run the main scraper**
````
python Tic_Tac_Toe.py
````

## Repo structure

```
TIC_TAC_TOE_GAME
├── README.md
└── Tic_Tac_Toe.py
```

## Usage (How to Play)

- **Start the Game**: Run the Python script (python Tic_Tac_Toe.py). The initial 3x3 board will be displayed with row and column numbers.

    ```
        0   1   2
    -------------
    0 |   |   |   |
    -------------
    1 |   |   |   |
    -------------
    2 |   |   |   |
    -------------
    ```

- **Player X starts first.**

- **On your turn (Player X or O):**
    - Enter the row number (0–2) when prompted.

    - Enter the column number (0–2) when prompted.

    The program validates the input (checking boundaries and if the cell is empty) and updates the board display.

- **Game End**: Players alternate turns until either:
    - One player aligns three of their symbols horizontally, vertically, or diagonally (Win).

    - The board is full without a winner (Draw).

- **The game announces the result.**


## The Core Functionality

The game is organized into six functional components:

- **create_board()**: Creates and initializes the 3x3 game board, represented as a list of lists.

- **display_board(board)**: Prints the current game board to the console, including row and column numbers for user reference.

- **player_move(board, player)**: Handles the current player's input, validates the chosen row/column, and updates the board with the player's symbol.

- **check_winner(board, player)**: Determines if the specified player has won by checking all possible row, column, and diagonal winning conditions.

- **check_draw(board)**: Checks if the game has ended in a draw by verifying if all cells on the board are occupied.

- **main()**: Contains the main game loop, manages the flow of the game, alternates turns, and calls the check functions after each move.

## Timeline

This project was completed over **2 days**, adhering to a focused rapid development schedule.

## Personal Situation
This project was completed as a **personal initiative** to practice and solidify several core Python programming concepts in a practical, self-contained application.

Connect with me on [LinkedIn](https://www.linkedin.com/in/zivile-butkute/).



[![Gaming GIF](https://media.tenor.com/2a4KThsm4YgAAAAj/gaming-game-on.gif)](https://tenor.com/en-GB/view/gaming-game-on-game-time-video-games-its-game-time-gif-25910808)  
*Image source: [tenor](https://tenor.com/en-GB/view/gaming-game-on-game-time-video-games-its-game-time-gif-25910808)*