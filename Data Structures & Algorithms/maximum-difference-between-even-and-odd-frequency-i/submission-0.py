class Solution:
    def maxDifference(self, s: str) -> int:
        hash_table = {}
        for letter in s:
            if letter in hash_table:
                hash_table[letter] += 1
            else:
                hash_table[letter] = 1

        frequencies = hash_table.values()
        
        max_odd = max((freq for freq in frequencies if freq % 2 != 0), default=0)
        min_even = min((freq for freq in frequencies if freq % 2 == 0), default=0)

        return max_odd - min_even