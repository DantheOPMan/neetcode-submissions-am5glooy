class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r = len(heights)-1
        res = 0
        while l < r:
            vol = (r - l) * min(heights[l],heights[r])
            res = max(vol, res)
            if heights[l] > heights[r]:
                r -=1
            else:
                l+=1
        return res