class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)

        for c in range(9):
            for r in range(9):
                n = board[r][c]
                if n == ".":
                    continue
                if n in rows[c] or n in cols[r] or n in boxs[(c//3,r//3)]:
                    return False

                rows[c].add(n)
                cols[r].add(n)
                boxs[c//3,r//3].add(n)
        return True