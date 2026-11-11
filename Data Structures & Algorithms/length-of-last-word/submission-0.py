class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        tmp = 0
        for letter in s:
            if letter == ' ':
                if result != 0:
                    tmp = result
                result = 0
            else:
                result += 1

        return result if result != 0 else tmp