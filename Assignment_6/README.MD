# Tic Tac Toe and Spirograph Project

This repository contains two Python projects:

Tic Tac Toe Game: A classic two-player game implemented using Python. Players take turns placing their marks (X or O) on a 3x3 grid. The first player to get three marks in a row (horizontally, vertically, or diagonally) wins. In case of a tie (all cells filled without a winner), the game declares a draw.
Spirograph: This code generates a dynamic spirograph using the Turtle graphics library. It creates a visually appealing pattern with colorful segments, customizable based on the number of segments and color randomization.
Tic Tac Toe Game 

 ## Dependencies:

pyfiglet library Used for creating an ASCII art title for the game.

turtle (included in the standard Python library): Provides Turtle graphics functionalities for drawing shapes.

## Gameplay:

The game starts with an ASCII art title displayed using pyfiglet.
The game board is shown, initially empty with "-" in each cell.
Players take turns entering row and column coordinates (0-2) to place their marks (X or O).
The game validates user input to ensure valid coordinates and empty cells.
The game checks for a winner (three marks in a row) after each turn.
If there's a winner, the game congratulates the winning player and exits.
If all cells are filled without a winner, the game declares a draw and exits.
Spirograph 


### Customization (Optional):

While the code generates a dynamic spirograph with random colors, you can modify the following variables in spirograph.py to customize the output:
colors: A list of color names used for randomization. Add or remove colors to change the palette.
i: The number of segments in the spirograph. Higher values create more complex patterns.
Contribution

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and create a pull request.

## License

This repository is distributed under the MIT License (https://opensource.org/license/mit). You are free to use, modify, and distribute the code under the terms of this license.

## Additional Notes

Consider including error handling for invalid user input in the Tic Tac Toe game.

At the end, I hope this improved README provides clear instructions, explanations, and guidance for both Python projects in your repository!
