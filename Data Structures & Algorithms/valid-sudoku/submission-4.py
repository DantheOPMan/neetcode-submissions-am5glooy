class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxs = defaultdict(list)

        for c in range(9):
            for r in range(9):
                value = board[c][r]
                if value == ".":
                    continue
                if value in rows[c] or value in cols[r] or value in boxs[c//3,r//3]:
                    return False
                rows[c].append(value)
                cols[r].append(value)
                boxs[c//3,r//3].append(value)
        return True
