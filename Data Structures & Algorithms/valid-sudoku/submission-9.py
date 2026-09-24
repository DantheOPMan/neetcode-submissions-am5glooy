class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)

        for c in range(9):
            for r in range(9):
                char = board[r][c]

                if char == ".":
                    continue
                if char in rows[c] or char in cols[r] or char in boxs[c // 3,r // 3]:
                    return False

                rows[c].add(char)
                cols[r].add(char)
                boxs[c // 3,r // 3].add(char)

        return True