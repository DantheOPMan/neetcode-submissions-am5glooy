class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxCount = 0
        data = {}
        res = 0
        for i, c in enumerate(s):
            data[c] = data.get(c,0) +1
            maxCount = max(maxCount, data[c])
            while (i - left + 1) - maxCount > k:
                data[s[left]] -= 1
                left +=1
            res = max(res, i-left+1)
        return res
