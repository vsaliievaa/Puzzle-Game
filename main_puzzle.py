"""git repo link: https://github.com/vsaliievaa/Puzzle-Game """


def read_input(path):
    """
    Takes a path to the .txt file as a string and returns a game board
    as a list of strings.
    """
    board = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            board.append(line.strip())
    return board


def form_columns(board: list) -> list:
    """
    Takes the game board as a list of rows, "rotates" it and returns a list of columns.

    >>> form_columns(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    ['****  3  ', '***  6   ', '** 4   82', '*1       ', '  31 81  ',\
 '****93 2*', '****   **', '****5 ***', '**** ****']
    """
    columns = []
    for i in range(len(board)):
        col = []
        for j in range(len(board[i])):
            col.append(board[j][i])
        columns.append(''.join(col))
    return columns


def uniqueness_check(board: list) -> bool:
    """
    Checks the given rows for uniqueness. Returns True
    if numbers from 1 to 9 are in a given row, False otherwise.

    """
    for i in range(len(board)):
        lst = []
        for j in range(len(board[i])):
            if board[i][j] not in lst or board[i][j] in [' ', '*']:
                lst.append(board[i][j])
            else:
                return False
    return True


def colored_blocks(board: list) -> list:
    """
    Takes a game board and forms a list of lists, which represents
    coloured blocks on this board. Each colored block consists of 9 cells.
    """
    vertical_blocks, horizontal_blocks, blocks = [], [], []
    a, b = 0, 5
    c, d = 4, 9
    for i in range(4, -1, -1):
        row = []
        for j in range(a, b):
            row.append(board[j][i])
        vertical_blocks.append(''.join(row))
        a += 1
        b += 1
    for i in range(4, 9):
        row = []
        for j in range(c, d):
            row.append(board[i][j])
        horizontal_blocks.append(''.join(row))
        c -= 1
        d -= 1
    for i in range(len(horizontal_blocks)):
        row = []
        row = horizontal_blocks[i] + vertical_blocks[i]
        blocks.append(row)
    return blocks


def validate_board(path: str) -> bool:
    """
    Main function. Returns True if all three rules are satisfied for the given board
    and False otherwise.
    """
    board = read_input(path)
    if uniqueness_check(board) and uniqueness_check(form_columns(board)):
        if uniqueness_check(colored_blocks(board)):
            return True
    return False
