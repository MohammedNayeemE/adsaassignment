def solve_n_queens(n):
    def is_safe(board, row, col):
       
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve(row):
        if row == n:
            
            solutions.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve(row + 1)
                board[row][col] = '.'

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve(0)
    return solutions

def print_solutions(solutions):
    for i, solution in enumerate(solutions, start=1):
        print(f"Solution {i}:")
        for row in solution:
            print(row)
        print()


N = 8  
solutions = solve_n_queens(N)
print_solutions(solutions)