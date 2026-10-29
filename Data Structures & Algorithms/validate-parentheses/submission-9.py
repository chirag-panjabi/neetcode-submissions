class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        # pairs = { '{':'}','(':')','[':']'}
        # for c in s:
        #     if c in pairs:
        #         stk.append(c)
        #     elif pairs[stk[-1]] == c:
        #         stk.pop()
        #     else:
        #         return False
        
        pairs = { '}':'{',']':'[',')':'('}
        for c in s:
            if c not in pairs:
                stk.append(c)
            else:
                if stk:
                    if stk[-1] == pairs[c]:
                        stk.pop()
                    else:
                        return False
                else:
                    return False

        return True if not stk else False
            
