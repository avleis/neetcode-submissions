class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            seen[i] = nums[i]
            for j in range(i + 1, len(nums)):
                if seen[i] + nums[j] == target:
                    return [i, j]
        return []