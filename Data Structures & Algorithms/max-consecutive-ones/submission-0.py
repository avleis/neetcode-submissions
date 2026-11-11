class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        result = 0
        for num in nums:
            if num == 1:
                counter += 1
            else:
                if counter > result:
                    result = counter
                counter = 0
        else: 
            if counter > result: result = counter
        return result
