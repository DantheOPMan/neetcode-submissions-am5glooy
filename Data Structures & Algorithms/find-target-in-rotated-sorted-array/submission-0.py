class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        
        while l < r:
            m = l + ((r - l) // 2)
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m

        pivot = l

        def binarySearch(left: int, right: int) -> int:
            while left <= right:
                m = left + ((right - left) // 2)
                if nums[m]  ==  target:
                    return m
                elif nums[m] < target:
                    left = m + 1
                else:
                    right = m -1 
            return -1

        res = binarySearch(0, pivot-1)
        if res != -1:
            return res
        
        return binarySearch(pivot, len(nums)-1)

                