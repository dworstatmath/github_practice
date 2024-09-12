import sys

# Define chess piece symbols
PIECES = {
    'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔',
    'p': '♟', 'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚',
    '.': '.'
}

# Initialize the board with pieces in starting positions
def initialize_board():
    board = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]
    return board

def print_board(board):
    for row in board:
        print(' '.join(PIECES.get(piece, piece) for piece in row))
    print()

def is_valid_position(pos):
    return 0 <= pos[0] < 8 and 0 <= pos[1] < 8

def move_piece(board, start, end):
    if not is_valid_position(start) or not is_valid_position(end):
        print("Invalid position.")
        return False

    piece = board[start[0]][start[1]]
    if piece == '.':
        print("No piece at start position.")
        return False

    # Move piece
    board[end[0]][end[1]] = piece
    board[start[0]][start[1]] = '.'
    return True

def main():
    board = initialize_board()
    print_board(board)

    while True:
        move = input("Enter your move (e.g., 'e2 e4'): ").strip()
        if move.lower() == 'quit':
            print("Game ended.")
            break
        
        try:
            start_pos, end_pos = move.split()
            start = (8 - int(start_pos[1]), ord(start_pos[0]) - ord('a'))
            end = (8 - int(end_pos[1]), ord(end_pos[0]) - ord('a'))
            
            if move_piece(board, start, end):
                print_board(board)
            else:
                print("Move failed. Try again.")
        except ValueError:
            print("Invalid input. Please enter moves in the format 'e2 e4'.")

if __name__ == "__main__":
    main()