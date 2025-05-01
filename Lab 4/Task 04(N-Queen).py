class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n  
        self.solutions = []  
    def solve(self):
        """Main function to solve N-Queens problem."""
        self.solve_util(0)
        return self.solutions

    def solve_util(self, row):
        """Helper function to solve N-Queens using backtracking."""
        
        if row == self.n:
            self.add_solution()
            return
        
        for col in range(self.n):
            
            if self.is_safe(row, col):
                
                self.board[row] = col
                self.solve_util(row + 1)
                
                self.board[row] = -1

    def is_safe(self, row, col):
        """Check if it's safe to place a queen at (row, col)."""
        for i in range(row):
            
            if self.board[i] == col or abs(self.board[i] - col) == abs(i - row):
                return False
        return True

    def add_solution(self):
        """Store the solution."""
        solution = []
        for row in range(self.n):
            
            row_str = ['.'] * self.n
            row_str[self.board[row]] = 'Q'
            solution.append(''.join(row_str))
        self.solutions.append(solution)

    def print_solutions(self):
        """Print all solutions."""
        if not self.solutions:
            print("No solution exists.")
        else:
            for idx, solution in enumerate(self.solutions):
                print(f"Solution {idx + 1}:")
                for row in solution:
                    print(row)
                print()

# Example 
n = 8  
nqueens = NQueens(n)
nqueens.solve()
nqueens.print_solutions()
