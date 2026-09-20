class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = {}
        longest = 0
        left = 0
        for i, c in enumerate(s):
            if c in tracker:
                left = max(left, tracker[c] + 1)
            tracker[c] = i
            longest = max(longest, i - left + 1)
        return longest