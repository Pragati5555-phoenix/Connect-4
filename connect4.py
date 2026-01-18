import sys

# --- Config ---
NUM_ROWS = 6
NUM_COLS = 7

EMPTY = ' '
PLAYER1 = 'X'
PLAYER2 = 'O'

# Board: list of columns, each column is a list bottom-up (index 0 is bottom)
_board = [[] for _ in range(NUM_COLS)]

# --- Board ops ---
def reset_board():
    global _board
    _board = [[] for _ in range(NUM_COLS)]

def drop_token(col, token):
    """Drop a token into the given column (0-based). Returns True on success."""
    if not (0 <= col < NUM_COLS):
        return False
    if len(_board[col]) >= NUM_ROWS:
        return False
    _board[col].append(token)
    return True

def get_square(row, col):
    """Get token at (row, col) where row 1 is bottom. Returns EMPTY if none."""
    if not (0 <= col < NUM_COLS and 1 <= row <= NUM_ROWS):
        return None
    if row <= len(_board[col]):
        return _board[col][row - 1]
    return EMPTY

def board_full():
    return all(len(col) == NUM_ROWS for col in _board)

# --- Rendering ---
def draw_board():
    """Render the board in the stylized ASCII format."""
    # Header
    print("\n   " + "   ".join(chr(ord('A') + c) for c in range(NUM_COLS)))
    print("__" + " " * (NUM_COLS * 4 - 1) + "__")
    # Rows top to bottom
    for r in range(NUM_ROWS, 0, -1):
        row_str = "||"
        for c in range(NUM_COLS):
            row_str += f" {get_square(r, c)} |"
        row_str = row_str[:-1] + "||"
        print(row_str)
        sep = "|+" + ("---+" * NUM_COLS)
        print(sep[:-1] + "|")
    print("^^" + " " * (NUM_COLS * 4 - 1) + "^^\n")

# --- Win check ---
def check_winner(token):
    """Return True if token has 4-in-a-row anywhere."""
    # Horizontal
    for r in range(1, NUM_ROWS + 1):
        for c in range(NUM_COLS - 3):
            if all(get_square(r, c + i) == token for i in range(4)):
                return True
    # Vertical
    for c in range(NUM_COLS):
        for r in range(1, NUM_ROWS - 2):
            if all(get_square(r + i, c) == token for i in range(4)):
                return True
    # Diagonal /
    for r in range(4, NUM_ROWS + 1):
        for c in range(NUM_COLS - 3):
            if all(get_square(r - i, c + i) == token for i in range(4)):
                return True
    # Diagonal \
    for r in range(1, NUM_ROWS - 2 + 1):
        for c in range(NUM_COLS - 3):
            if all(get_square(r + i, c + i) == token for i in range(4)):
                return True
    return False

# --- Input helpers ---
def read_move(prompt="Choose a column (A-G): "):
    """Read a column letter A-G (case-insensitive). Returns 0-based col or None."""
    s = input(prompt).strip().upper()
    if len(s) != 1 or not ('A' <= s <= chr(ord('A') + NUM_COLS - 1)):
        return None
    return ord(s) - ord('A')

def read_yes_no(prompt="Play again? (y/n): "):
    s = input(prompt).strip().lower()
    return s.startswith('y')

# --- Game loop ---
def play_game():
    reset_board()
    print("Welcome to Connect Four!")
    print("Players:")
    print(f"  Player {PLAYER1} vs Player {PLAYER2}")
    draw_board()

    current = PLAYER1
    while True:
        col = read_move(f"Player {current}, choose a column (A-{chr(ord('A')+NUM_COLS-1)}): ")
        if col is None:
            print("Invalid column. Enter a single letter in range.")
            continue
        if not drop_token(col, current):
            print("Column full. Try a different column.")
            continue

        draw_board()

        if check_winner(current):
            print(f"Player {current} wins! 🎉")
            break
        if board_full():
            print("It's a draw! 🤝")
            break

        current = PLAYER2 if current == PLAYER1 else PLAYER1

def main():
    try:
        while True:
            play_game()
            if not read_yes_no():
                print("Thanks for playing!")
                break
            print("\n" + "-" * 48 + "\n")
    except (KeyboardInterrupt, EOFError):
        print("\n\nThanks for playing!")
        sys.exit(0)

if __name__ == "__main__":
    main()



