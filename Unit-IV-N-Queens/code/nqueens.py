def is_safe(board, row, col, n):
    # Check the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    # All queens are placed
    if row == n:
        print_solution(board, n)
        return 1

    count = 0

    # Try every column in the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col

            count += solve_n_queens(board, row + 1, n)

            # Backtracking
            board[row] = -1

    return count


def print_solution(board, n):
    print("\nSolution:")

    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


n = 4
board = [-1] * n

print("N-Queens Problem")
print("N =", n)

solutions = solve_n_queens(board, 0, n)

print("\nTotal solutions:", solutions)