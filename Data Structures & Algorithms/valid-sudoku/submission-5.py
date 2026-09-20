class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(list)
        columns = defaultdict(list)
        boxs = defaultdict(list)

        for c in range(9):
            for r in range(9):
                d = board[c][r]
                if d == ".":
                    continue
                if d in rows[c] or d in columns[r] or d in boxs[c // 3,r //3 ]:
                    return False
                rows[c].append(d)
                columns[r].append(d)
                boxs[c //3,r //3].append(d)

        return True