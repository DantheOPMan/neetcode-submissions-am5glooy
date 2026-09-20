class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height)-1
        lMax = height[l]
        rMax = height[r]
        while l < r:
            if lMax > rMax:
                res += rMax - height[r]
                r-=1
                rMax = max(rMax, height[r])
            else:
                res += lMax - height[l]
                l+=1
                lMax = max(lMax, height[l])
        return res
