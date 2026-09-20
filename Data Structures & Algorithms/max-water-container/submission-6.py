class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights)-1
        maxValue = 0

        while l < r:


            maxValue = max(maxValue, (r - l) * min(heights[r], heights[l]))
            if heights[l] < heights[r]:
                l+=1
            else:
                r -=1

        return maxValue