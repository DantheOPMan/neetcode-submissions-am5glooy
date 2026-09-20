class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longest = 0
        for n in nums:
            curLength = 0
            if n-1 not in values:
                while (n + curLength) in values:
                    curLength+= 1

                longest = max(curLength, longest)


        return longest