class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = {}
        l = 0
        res = 0
        for i in range(len(s)):
            
            if s[i] in data:
                l = max(data[s[i]]+1,l)
            
            res = max(i-l+1, res)
            data[s[i]] = i
        return res