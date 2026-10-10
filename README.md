# Ultimate Tic Tac Toe

## Overview

**Ultimate Tic Tac Toe** is a two-player strategy game built with Python and Pygame. It expands the classic Tic Tac Toe game into a larger board consisting of nine smaller boards.

Players take turns placing their marks (`X` and `O`) on the board. The goal is to win three small boards in a row on the main board.

## Features

- Two-player local gameplay.
- Interactive graphical interface.
- Nine smaller Tic Tac Toe boards arranged in a 3×3 grid.
- Highlighting of the active board.
- Automatic detection of winning combinations.
- Draw detection.
- Restart functionality.
- On-screen instructions and game results.

## Requirements

- Python 3.8 or newer
- Pygame

## Installation

1. Clone or download the repository.
2. Navigate to the project directory.
3. Install the required dependency:

```bash
pip install pygame
```

## Usage

Run the following command from the project directory:

```bash
python main.py
```

Replace `main.py` with the name of the file containing the main game loop if it is different.

## Controls

| Key / Action | Description |
|---|---|
| `Enter` | Start the game |
| Left mouse button | Place a mark in an available cell |
| `R` | Reset the game |
| `Esc` | Exit the game |

You can also start the game by clicking the mouse button on the start screen.

## Game Rules

1. The game begins with an empty 3×3 grid of smaller Tic Tac Toe boards.
2. Players take turns placing `X` and `O` in empty cells.
3. The position of a move determines which small board the opponent must play in next. For example, playing in the top-right cell sends the opponent to the top-right small board.
4. If the designated small board has already been won or is full, the next player can choose any available board.
5. A player wins a small board by forming a horizontal, vertical, or diagonal line of three marks.
6. A player wins the game by winning three small boards in a horizontal, vertical, or diagonal line.
7. If all small boards are completed without a player winning the main board, the game ends in a draw.

## Technologies

- **Python** — game logic and application structure.
- **Pygame** — graphics, mouse input, keyboard events, and the game window.

## Project Structure

```text
project/
├── main.py
├── Game.py
├── BigBoard.py
├── MiniBoard.py
├── Cell.py
├── Renderer.py
└── Constants.py
```
