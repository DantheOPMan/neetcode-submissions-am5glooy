class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for _ in range(len(nums))]
        print(output)

        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = postfix * output[i]
            postfix = postfix * nums[i]
        return output