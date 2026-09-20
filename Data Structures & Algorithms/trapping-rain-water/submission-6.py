class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax = height[l]
        rMax = height[r]
        total = 0
        while l < r:
            if lMax > rMax:
                r-=1
                rMax = max(height[r], rMax)
                total += rMax - height[r]
            else:
                l+=1
                lMax = max(height[l], lMax)
                total += lMax - height[l]

        return total