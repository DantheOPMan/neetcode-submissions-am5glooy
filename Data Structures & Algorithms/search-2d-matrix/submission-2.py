class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = ROWS * COLS - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            col = mid // COLS
            row = mid % COLS

            if target > matrix[col][row]:
                l = mid + 1
            elif target < matrix[col][row]:
                r = mid - 1
            else:
                return True

        return False
            