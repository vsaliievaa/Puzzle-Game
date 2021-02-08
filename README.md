This module allows the user to play a simple puzzle game, a simplified version of sudoku.
The game board is 9*9 cells and consists of white and coloured cells (white regions are not used for the game). To start playing, the game board should be filled with numbers according to the next rules:
1) Coloured cells of each row should contain numbers from 1 to 9 without repetitions.
2) Coloured cells of each column should contain numbers from 1 to 9 without repetitions.
3) Blocks of cells of each colour should contain numbers from 1 to 9 without repetitions.

The main function of this module, validate_board(), takes in a game board as a list of strings and returns True, if the board satisfies all the rules, and False otherwise.
form_columns() takes a board as a list of strings, 'rotates' it and returns a list of columns.
uniqueness_check() takes a board as a list of strings and checks every string (i.e. row or column) for uniqueness.
colored_blocks() takes a board as a list of strings, forms a list of string, representing coloured blocks, and returns it.
