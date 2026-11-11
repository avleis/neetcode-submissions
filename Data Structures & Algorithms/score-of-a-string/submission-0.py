class Solution:
    def scoreOfString(self, s: str) -> int:
        nums = []
        r = 0

        for i in range(len(s)):
            nums.append(ord(s[i]))

        for j in range(len(nums) - 1):
            r += abs((nums[j + 1]) - nums[j])

        return r

        