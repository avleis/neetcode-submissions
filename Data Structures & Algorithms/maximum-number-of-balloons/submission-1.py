class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_map = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        target = "balloon"
        result = 0

        for letter in text:
            if letter in hash_map:
                hash_map[letter] += 1
        
        while 0 not in hash_map.values():
            for letter in target:
                if hash_map[letter] >= 1:
                    hash_map[letter] -= 1
                else: return result
            result += 1
        return result