class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:

            x = l + ((r - l) // 2)
            if nums[x] > target:
                r = x -1
            elif nums[x] < target:
                l = x + 1
            else:
                return x
        
        return -1