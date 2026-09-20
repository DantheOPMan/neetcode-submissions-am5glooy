class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = {}
        l = 0
        res = 0
        for i in range(len(s)):
            if s[i] in data:
                l = max(data[s[i]] + 1, l)
            data[s[i]] = i
            res = max(res, i - l + 1)
            print(s[i])
            print(i)
            print(l)
            print(res)
        return res            