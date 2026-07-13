#!/usr/bin/python3
"""Solves the N queens puzzle.

Determines all the possible solutions to placing N non-attacking
queens on an N x N chessboard.

Example:
    $ ./101-nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]
"""
import sys


def is_safe(positions, row, col):
    """Check if a queen can be placed at (row, col).

    Args:
        positions (list): The columns of queens placed on previous rows.
        row (int): The row of the queen to place.
        col (int): The column of the queen to place.

    Returns:
        bool: True if no previously placed queen attacks (row, col).
    """
    for prev_row, prev_col in enumerate(positions):
        if prev_col == col:
            return False
        if abs(prev_col - col) == abs(prev_row - row):
            return False
    return True


def solve(n, row, positions, solutions):
    """Recursively place queens row by row using backtracking.

    Args:
        n (int): The size of the board.
        row (int): The current row to place a queen in.
        positions (list): The columns of queens placed so far.
        solutions (list): The accumulated list of full solutions.
    """
    if row == n:
        solutions.append(list(positions))
        return
    for col in range(n):
        if is_safe(positions, row, col):
            positions.append(col)
            solve(n, row + 1, positions, solutions)
            positions.pop()


def main():
    """Parse arguments, validate them, and print all N queens solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve(n, 0, [], solutions)
    for solution in solutions:
        print([[row, col] for row, col in enumerate(solution)])


if __name__ == "__main__":
    main()
