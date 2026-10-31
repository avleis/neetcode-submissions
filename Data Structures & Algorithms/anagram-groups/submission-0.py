class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        anagrams_map = {}
        for word in words:
            sorted_key = "".join(sorted(word))
            if sorted_key in anagrams_map:
                anagrams_map[sorted_key].append(word)
            else:
                anagrams_map[sorted_key] = [word]
        return list(anagrams_map.values())