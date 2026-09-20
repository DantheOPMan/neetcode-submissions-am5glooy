class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        i,j = 0,len(height)-1
        left, right = height[i], height[j]
        while i < j:
            if left < right:
                i+=1
                left = max(left, height[i])
                area += left - height[i]
            else:
                j-=1
                right = max(right,height[j])
                area += right - height[j]
        return area