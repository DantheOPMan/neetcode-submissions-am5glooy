class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        data = {}
        res = 0
        maxC = 0
        l = 0
        for i in range(len(s)):
            data[s[i]] = data.get(s[i],0) + 1
            maxC = max(maxC, data[s[i]])
            while (i - l + 1) - maxC > k:
                data[s[l]] -= 1
                l +=1
            res = max(res, i-l+1)
        return res