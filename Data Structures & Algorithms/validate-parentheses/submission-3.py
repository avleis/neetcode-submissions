class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        stack = []

        for paranthes in s:
            if paranthes in '[{(':
                stack.append(paranthes)
            elif paranthes in ']})':
                if not stack:
                    return False
                
                open_bracket = stack.pop()

                if open_bracket == '(' and paranthes == ')':
                    continue
                elif open_bracket == '[' and paranthes == ']':
                    continue
                elif open_bracket == '{' and paranthes == '}':
                    continue
                else: 
                    return False
                    
        if not stack:
            return True
        else: 
            return False