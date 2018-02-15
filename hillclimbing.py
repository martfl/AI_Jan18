from random import randint


def main():
    n = input("Size N of board (N x N) defaults to 8: ")
    try:
        n = int(n)
    except ValueError:
        n = 8
    m = input("Max number of restarts (empty for infinite restarts): ")
    try:
        int(m)
    except ValueError:
        m = -1
    s = input("Allow side steps?(y/n): ")
    if s == 'n':
        sidestep = False
    else:
        sidestep = True

    board = create_board(n)
    print_board(board)
    solved_board = hill_climbing(board, m, sidestep)
    if solved_board is None:
        print("No solution found")
    else:
        print_board(solved_board)


def create_board(n):
    board = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        queen = randint(0, n - 1)
        board[i][queen] = 'Q'
    return board


def hill_climbing(board, m, s):
    h = get_pairs(board)
    cycles = 0
    while h != 0:
        if cycles == m: return None
        board = make_move(board, s)
        h = get_pairs(board)
        cycles += 1
    return board


def make_move(board, s):
    moves = {}
    for i in range(len(board)):
        queen = board[i].index('Q')
        for j in range(len(board)):
            board_copy  = [[i for i in row] for row in board]
            board_copy[i][j], board_copy[i][queen] = board_copy[i][queen], board_copy[i][j]
            moves[(i,j)] = get_pairs(board_copy)

    best_moves = []
    h_to_beat = get_pairs(board)
    for x in moves.keys():
        if moves[x] < h_to_beat:
            h_to_beat = moves[x]
    for x in moves.keys():
        if moves[x] == h_to_beat:
            best_moves.append(x)

    if s or len(best_moves) > 1:
        pick = randint(0, len(best_moves) - 1)
        i, j = best_moves[pick]
    else:
        i, j = best_moves[0]

    queen = board[i].index('Q')
    board[i][j], board[i][queen] = board[i][queen], board[i][j]
    return board


def get_pairs(board):
    n = len(board)
    h = 0
    d = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'Q':
                h -= 2
                # horizontal/vertical pairs
                for k in range(n):
                    if board[i][k] == 'Q':
                        h += 1
                    if board[k][j] == 'Q':
                        h += 1
                k, l = i + 1, j + 1
                # diagonal pairs
                while k < n and l < n:
                    if board[k][l] == 'Q':
                        d += 1
                    k += 1
                    l += 1
                k, l = i + 1, j - 1
                while k < n and l >= 0:
                    if board[k][l] == 'Q':
                        d += 1
                    k += 1
                    l -= 1
                k, l = i - 1, j + 1
                while k >= 0 and l < n:
                    if board[k][l] == 'Q':
                        d += 1
                    k -= 1
                    l += 1
                k, l = i - 1, j - 1
                while k >= 0 and l >= 0:
                    if board[k][l] == 'Q':
                        d += 1
                    k -= 1
                    l -= 1
    return int((d + h) / 2)


def print_board(board):
    n = len(board)
    for i in range(n):
        print('|', end='')
        for j in range(n):
            print(board[j][i] if board[j][i] == 'Q' else ' ', end='|')
        print("")
    print("")


if __name__ == '__main__':
    main()
