class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]

        while l < r:
            if maxL > maxR:
                area += maxR - height[r] 
                r-=1
                maxR = max(maxR, height[r])
            else:
                area += maxL - height[l]
                l+=1
                maxL = max(maxL, height[l])

        return area