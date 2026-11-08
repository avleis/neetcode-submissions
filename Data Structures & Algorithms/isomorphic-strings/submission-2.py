class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_table = {}
        used_in_t = set()

        for i, j in zip(s.lower(), t.lower()):
            if i in hash_table:
                if hash_table[i] != j:
                    return False
            else:
                if j in used_in_t:
                    return False

                hash_table[i] = j
                used_in_t.add(j)

        return True
        