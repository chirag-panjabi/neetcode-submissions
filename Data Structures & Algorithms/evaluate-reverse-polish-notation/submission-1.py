class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {'+', '-', '*', '/'}
        stk = []
        for t in tokens:
            if t in op:
                second = stk.pop()
                first = stk.pop()
                if t == '+':
                    stk.append(first + second)
                elif t == '-':
                    stk.append(first - second)
                elif t == '*':
                    stk.append(first * second)
                else:
                    stk.append(int(first / second))
            else:
                stk.append(int(t))
            
        return stk[-1]

