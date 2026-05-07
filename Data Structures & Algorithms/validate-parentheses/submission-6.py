class Solution:
    def isValid(self, s: str) -> bool:
        # stack approach from notes
        if len(s) % 2 != 0: return False
        
        valid = {'{':'}',
                 '[':']',
                 '(':')'}
        
        stack = []
        for br in s:
            if br in valid:
                stack.append(br)
            elif len(stack)>0 and valid[stack[-1]] == br:
                del stack[-1]
            else: 
                return False
        return len(stack) == 0
