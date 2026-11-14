class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_table = {}
    
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1  # Start count at 1
                
        # Use key=hash_table.get to find the key with the highest value
        return max(hash_table, key=hash_table.get)