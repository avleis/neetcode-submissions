class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_h = {}
        for letter in s:
            s_h[letter] = s_h.get(letter, 0) + 1
        for letter in t:
            if letter not in s_h or s_h[letter] == 0:
                return False
            s_h[letter] -= 1
        return True