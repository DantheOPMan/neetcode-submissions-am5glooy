class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1

        lMax, rMax = height[l], height[r]
        area = 0
        while l < r:
            if lMax > rMax:
                r -=1
                rMax = max(rMax, height[r])
                area += max(0, rMax - height[r])
            else:
                l +=1
                lMax = max(lMax, height[l])
                area += max(0, lMax - height[l])

        return area