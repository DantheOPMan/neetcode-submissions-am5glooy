class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = set(nums)
        res = 0
        for n in data:
            if n-1 not in data:
                count = 1
                while (n + count) in data:
                    count+=1
                res = max(count, res)

        return res