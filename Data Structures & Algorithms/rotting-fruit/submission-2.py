class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append([r,c])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r,c = q.popleft()
                for rchange, cchange in directions:
                    rnew, cnew = r + rchange, c + cchange
                    if rnew in range(ROWS) and cnew in range(COLS) and grid[rnew][cnew] == 1:
                        fresh-=1
                        grid[rnew][cnew] = 2
                        q.append([rnew,cnew])
            time +=1

        return time if fresh == 0 else -1