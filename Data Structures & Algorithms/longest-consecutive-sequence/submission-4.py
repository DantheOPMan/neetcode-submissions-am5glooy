class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mappings = defaultdict(int)
        longest = 0
        for n in nums:
            if not mappings[n]:
                mappings[n] = mappings[n+1] + mappings[n-1] + 1
                mappings[n - mappings[n-1]] = mappings[n]
                mappings[n + mappings[n+1]] = mappings[n]
                longest = max(longest, mappings[n])
        return longest