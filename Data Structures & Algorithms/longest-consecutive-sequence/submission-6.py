class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = set(nums)
        longest = 0
        for n in data:
            if n-1 not in data:
                cur = 0
                while n + cur in data:
                    cur+=1
                longest = max(longest, cur)

        return longest