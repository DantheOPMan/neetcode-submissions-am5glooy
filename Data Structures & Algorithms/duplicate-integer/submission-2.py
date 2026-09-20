class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unq = set()
        for n in nums:
            if n in unq:
                return True
            unq.add(n)
        return False