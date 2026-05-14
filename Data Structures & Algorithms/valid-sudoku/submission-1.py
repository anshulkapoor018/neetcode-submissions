from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Track numbers seen in each column
        # Example:
        # cols[0] = {"5", "3"}
        cols = defaultdict(set)

        # Track numbers seen in each row
        rows = defaultdict(set)

        # Track numbers seen in each 3x3 square
        #
        # Key format:
        # (row // 3, col // 3)
        #
        # Example:
        # Top-left box     -> (0,0)
        # Top-middle box   -> (0,1)
        # Center box       -> (1,1)
        sq = defaultdict(set)

        # Traverse every cell in the 9x9 board
        for r in range(9):
            for c in range(9):

                val = board[r][c]

                # Ignore empty cells
                if val == ".":
                    continue

                # Check if number already exists in:
                # - current row
                # - current column
                # - current 3x3 square
                #
                # If yes -> Sudoku is invalid
                if (
                    val in rows[r]
                    or val in cols[c]
                    or val in sq[(r // 3, c // 3)]
                ):
                    return False

                # Add value into current row set
                rows[r].add(val)

                # Add value into current column set
                cols[c].add(val)

                # Add value into current 3x3 square set
                sq[(r // 3, c // 3)].add(val)

        # No duplicates found
        return True