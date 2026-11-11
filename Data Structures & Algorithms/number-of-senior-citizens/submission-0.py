class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for detail in details:
            if (int(detail[-4] + detail[-3])) > 60:
                counter += 1
        return counter