import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.geometry("450x550")
        self.root.config(bg="#1e1e2f")  # Dark background

        # Title
        title = tk.Label(
            self.root,
            text="Sudoku Solver",
            font=("Arial", 24, "bold"),
            bg="#1e1e2f",
            fg="#00f5d4",  # Neon teal
        )
        title.pack(pady=10)

        # Sudoku Grid
        self.cells = []
        grid_frame = tk.Frame(self.root, bg="#1e1e2f")
        grid_frame.pack()

        for i in range(9):
            row = []
            for j in range(9):
                entry = tk.Entry(
                    grid_frame,
                    width=2,
                    font=("Arial", 18),
                    bg="#16161d",  # Slightly lighter dark
                    fg="#ff99cc",  # Neon pink
                    justify="center",
                    insertbackground="#00f5d4",  # Neon teal cursor
                )
                entry.grid(row=i, column=j, padx=3, pady=3, ipady=10)
                row.append(entry)
            self.cells.append(row)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#1e1e2f")
        btn_frame.pack(pady=20)

        tk.Button(
            btn_frame,
            text="Solve Sudoku",
            font=("Arial", 14, "bold"),
            bg="#00f5d4",  # Neon teal
            fg="#1e1e2f",  # Dark background for contrast
            command=self.solve_sudoku,
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            btn_frame,
            text="Clear Grid",
            font=("Arial", 14, "bold"),
            bg="#ff99cc",  # Neon pink
            fg="#1e1e2f",
            command=self.clear_grid,
        ).grid(row=0, column=1, padx=10)

        # Footer
        footer = tk.Label(
            self.root,
            text="Developed by Rabuma",
            font=("Arial", 10, "italic"),
            bg="#1e1e2f",
            fg="#808080",  # Gray for footer
        )
        footer.pack(side=tk.BOTTOM, pady=10)

    def is_valid(self, grid, row, col, num):
        """Check if num can be placed at grid[row][col]."""
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
            if grid[row - row % 3 + i // 3][col - col % 3 + i % 3] == num:
                return False
        return True

    def solve(self, grid):
        """Solve the Sudoku using backtracking."""
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    def get_grid(self):
        """Get the current grid from the user input."""
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.cells[i][j].get().strip()
                if val.isdigit():
                    row.append(int(val))
                else:
                    row.append(0)
            grid.append(row)
        return grid

    def display_grid(self, grid):
        """Display the solved grid."""
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, str(grid[i][j]))

    def solve_sudoku(self):
        """Solve the Sudoku puzzle."""
        grid = self.get_grid()
        if self.solve(grid):
            self.display_grid(grid)
            messagebox.showinfo("Sudoku Solver", "Sudoku solved successfully!")
        else:
            messagebox.showerror("Sudoku Solver", "No solution exists for the given Sudoku.")

    def clear_grid(self):
        """Clear the Sudoku grid."""
        for row in self.cells:
            for cell in row:
                cell.delete(0, tk.END)

# Run the Sudoku Solver
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
