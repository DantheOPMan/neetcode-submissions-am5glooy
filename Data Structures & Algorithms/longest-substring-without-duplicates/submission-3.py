class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        longest, left = 0, 0
        for i in range(len(s)):
            while s[i] in letters:
                letters.remove(s[left])
                left += 1
            letters.add(s[i])
            longest = max(longest, i-left+1)
        return longest