class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        i,j = 0, len(heights)-1
        while i < j:
            height = min(heights[i],heights[j])
            area = height * (j-i)
            if area > mx:
                mx = area
            if(heights[i] == height):
                i+=1
            else:
                j-=1
        return mx
        