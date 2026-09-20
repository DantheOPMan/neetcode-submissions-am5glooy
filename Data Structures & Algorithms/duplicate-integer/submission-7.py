class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = set(nums)
        return len(data) != len(nums)