class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        for r in range(9):
            for c in range(9):
                tile = board[r][c]
                if tile == ".":
                    continue
                if tile in rows[c] or tile in cols[r] or tile in box[r//3,c//3]:
                    return False
                rows[c].add(tile)
                cols[r].add(tile)
                box[r//3,c//3].add(tile)
        return True