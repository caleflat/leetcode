from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        found = {} # column idx: { values }
        for row in board:
            for (i, col) in enumerate(row):
                if i in found:
                    found[i] = found[i].append(col)
                else:
                    found[i] = [col]

