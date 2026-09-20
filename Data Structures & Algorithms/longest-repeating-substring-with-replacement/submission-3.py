class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        data = {}
        left = 0
        maxCount = 0
        res = 0
        for i in range(len(s)):
            print(s[i])
            print(left)
            print(i)
            data[s[i]] = data.get(s[i],0) + 1
            maxCount = max(data[s[i]], maxCount)
            while (i - left + 1) - maxCount > k:
                data[s[left]] -= 1
                left +=1
            res = max(res, i-left+1)

        return res