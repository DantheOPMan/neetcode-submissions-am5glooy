class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        col = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                if value in rows[c] or value in col[r] or value in boxes[r//3,c//3]:
                    return False
                rows[c].add(value)
                col[r].add(value)
                boxes[r//3,c//3].add(value)
        return True