class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        int_dict = {}
        for num in nums:
            if num not in int_dict:
                int_dict[num] = 1
            elif int_dict[num] == 1:
                return True
        return False