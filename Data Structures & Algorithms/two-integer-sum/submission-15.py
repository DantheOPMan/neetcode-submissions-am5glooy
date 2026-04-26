class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difs = {}

        for i in range(len(nums)):
            dif = target-nums[i]
            if dif in difs:
                return [difs[dif], i]
            difs[nums[i]] = i
        
        return []