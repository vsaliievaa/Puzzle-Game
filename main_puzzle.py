"""git repo link: https://github.com/vsaliievaa/Puzzle-Game """


def form_columns(board: list) -> list:
    """
    Takes the game board as a list of rows, "rotates" it and returns a list of columns.

    >>> form_columns(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    ['****  3  ', '***  6   ', '** 4   82', '*1       ', '  31 81  ',\
 '****93 2*', '****   **', '****5 ***', '**** ****']
    >>> form_columns(["****9****", "***98****", "**987****", "*9876****",\
        "987654321", "87654321*", "7654321**", "654321***", "54321****"])
    ['****98765', '***987654', '**9876543', '*98765432', '987654321',\
 '****4321*', '****321**', '****21***', '****1****']
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

    >>> uniqueness_check(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> uniqueness_check(['****  3  ', '***  6   ', '** 4   82', '*1       ', '  31 81  ',\
        '****93 2*', '****   **', '****5 ***', '**** ****'])
    False
    >>> uniqueness_check(['****98765', '***987654', '**9876543', '*98765432',\
        '987654321', '****4321*', '****321**', '****21***', '****1****'])
    True
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

    >>> colored_blocks(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    [' 9 5   31', ' 83  1   ', '  1   4  ', ' 8  2  6 ', '  2    3 ']
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
        row = horizontal_blocks[i] + vertical_blocks[i][0:-1]
        blocks.append(row)
    return blocks


def validate_board(board: list) -> bool:
    """
    Main function. Returns True if all three rules are satisfied for the given board
    and False otherwise.

    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(['****98765', '***987654', '**9876543', '*98765432',\
        '987654321', '****4321*', '****321**', '****21***', '****1****'])
    True
    """
    if uniqueness_check(board) and uniqueness_check(form_columns(board)):
        if uniqueness_check(colored_blocks(board)):
            return True
    return False
