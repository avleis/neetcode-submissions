class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = {}
        words = s.split()
        if len(words) != len(pattern):
            return False  
        for index, word in enumerate(words):
            if word in pattern_map.values():
                if pattern_map.get(pattern[index]) != word:
                    return False
            else:
                if pattern[index] in pattern_map:
                    return False
                pattern_map[pattern[index]] = word
        return True