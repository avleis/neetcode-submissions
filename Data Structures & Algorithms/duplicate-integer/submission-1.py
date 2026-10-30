class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_nums = {}
        for num in nums:
            if num in hash_nums:
                return True
            else:
                hash_nums[num] = nums
        return False