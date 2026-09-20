class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        box = defaultdict(set)

        for c in range(9):
            for r in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                if value in cols[c] or value in rows[r] or value in box[(r//3,c//3)]:
                    return False
                cols[c].add(value)
                rows[r].add(value)
                box[(r//3,c//3)].add(value)

        return True