# N-Queens State Space Tree Using Backtracking

## Unit
Unit IV - Backtracking

## Project Number
Project 10

## Problem Title
N-Queens State Space Tree for N = 4

---

## 1. Objective

The objective of this project is to visualize the state-space tree of the N-Queens problem using the backtracking technique.

For N = 4, four queens must be placed on a 4 x 4 chessboard such that no two queens attack each other.

---

## 2. Problem Statement

The N-Queens problem is a classic backtracking problem.

The task is to place N queens on an N x N chessboard so that no two queens share the same row, column, or diagonal.

In this project, N = 4 is used to demonstrate recursive search and backtracking.

---

## 3. Algorithm

1. Start with an empty 4 x 4 chessboard.
2. Begin from the first row.
3. Try each column in the current row.
4. Check whether the position is safe.
5. If safe, place the queen and move to the next row.
6. If no safe position is available, backtrack.
7. Remove the previous queen and try another column.
8. Continue until all four queens are placed.
9. Record every valid arrangement.

---

## 4. Pseudocode

NQueens(board, row):

    if row == N:
        print solution
        return

    for each column in the current row:

        if position is safe:

            place queen

            NQueens(board, row + 1)

            remove queen

---

## 5. State-Space Tree

The state-space tree represents the choices made while placing queens row by row.

- Each level represents a row.
- Each branch represents a possible column.
- Invalid branches are rejected.
- Backtracking occurs when a branch cannot produce a solution.
- A complete path represents a valid solution.

---

## 6. AI Visualization Prompt

Create a clean academic state-space tree visualization for the N-Queens problem with N = 4.

Show the recursive process of placing four queens on a 4 x 4 chessboard, one queen per row.

Show valid and invalid branches. Mark invalid branches in red. Show backtracking and highlight valid solution paths in green.

Clearly label Row 1, Row 2, Row 3, and Row 4.

Use a professional academic style with a white background.

---

## 7. Visualization

The project includes an interactive HTML visualization:

visualization.html

The visualization demonstrates the root node, row-by-row queen placement, valid branches, invalid branches, backtracking, and valid solutions.

---

## 8. Python Implementation

The Python implementation is available in:

code/nqueens.py

The program recursively places queens and uses backtracking whenever a placement cannot lead to a solution.

---

## 9. Results

For N = 4, the algorithm finds two valid solutions.

### Solution 1

. Q . .
. . . Q
Q . . .
. . Q .

Column representation: [2, 4, 1, 3]

### Solution 2

. . Q .
Q . . .
. . . Q
. Q . .

Column representation: [3, 1, 4, 2]

Total number of solutions: 2

---

## 10. Complexity

Time Complexity: O(N!)

Space Complexity: O(N)

---

## 11. Conclusion

The N-Queens problem demonstrates how backtracking explores possible solutions while eliminating invalid choices.

The state-space tree makes the recursive decision process easier to understand.

For N = 4, the algorithm successfully finds two valid arrangements.

---

## 12. Tools Used

- Python - Algorithm implementation
- HTML, CSS, and JavaScript - Visualization
- AI tools - Visualization assistance
- GitHub - Repository and version control