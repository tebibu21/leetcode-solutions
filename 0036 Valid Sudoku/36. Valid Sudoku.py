from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # sets to track seen numbers for each row, column and 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                # compute box index: (r//3)*3 + (c//3)
                b = (r // 3) * 3 + (c // 3)
                # if value already seen in row/col/box -> invalid
                if val in rows[r] or val in cols[c] or val in boxes[b]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[b].add(val)

        return True
