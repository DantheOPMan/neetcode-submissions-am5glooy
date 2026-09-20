class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        data = {}
        left = 0
        for i, c in enumerate(s):
            if c in data:
                left = max(left, data[c] + 1)
            data[c] = i
            res = max(res, i - left + 1)
        return res