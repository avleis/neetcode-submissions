import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.translate(str.maketrans('', '', string.punctuation + string.whitespace)).lower()
        range_s = (len(s_lower) // 2) + 1
        
        for _ in range(range_s):
            if len(s_lower) <= 1:
                return True
            elif s_lower[0] == s_lower[-1]:
                s_lower = s_lower[1:-1]
            else:
                return False
