class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        int_dict = set()
        for num in nums:
            if num in int_dict:
                return True
            int_dict.add(num)
        return False