class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_hash = {}
        for num in nums:
            if num in nums_hash:
                nums_hash[num] += 1
            else:
                nums_hash[num] = 1
        
        result = []
        for i in range(0, k):
            max_key = max(nums_hash, key=nums_hash.get)
            result.append(max_key)
            nums_hash.pop(max_key)
        return result
        