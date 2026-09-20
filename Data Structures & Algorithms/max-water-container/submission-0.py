class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = 0
        for i, num in enumerate(heights):
            j = i+1
            while j < len(heights):
                if(j==6):
                    print(j)
                height = min(num, heights[j])
                area = height * (j-i)
                if area > mx:
                    mx = area
                j+=1

        return mx