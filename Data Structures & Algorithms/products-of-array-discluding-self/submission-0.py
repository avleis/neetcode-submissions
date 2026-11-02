class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        save_nums = nums.copy()
        len_nums = len(nums) 

        if len_nums == 1:
            return nums

        for i in range(len_nums):
            save_nums.pop(i)
            for j in range(len(save_nums)):
                output[i] *= save_nums[j]
            save_nums = nums.copy()
        return output