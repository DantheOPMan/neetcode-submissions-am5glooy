class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = {}
        left = 0
        maxLength = 0
        for i, n in enumerate(list(s)):
            if n in data:
                left = max(left, data[n] + 1)
            
            data[n] = i
            maxLength = max(maxLength, i - left + 1)

        return maxLength
