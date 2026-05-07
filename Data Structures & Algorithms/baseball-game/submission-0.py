class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        # for i in range(len(operations)):
        #     if operations[i] == "+":
        #         stack.append( stack[-1] + stack[-2] )
                # sum += stack[-1]
        #     elif operations[i] == "C":
                # sum -= stack[-1]
        #         del stack[-1]
        #     elif operations[i] == "D":
        #         stack.append( 2 * stack[-1] )
                # sum += stack[-1]
        #     else:
        #         stack.append(int(operations[i]))
                # sum += stack[-1]

        for i in operations:
            if i == "+":
                stack.append( stack[-1] + stack[-2] )
                sum += stack[-1]
            elif i == "C":
                sum -= stack[-1]
                del stack[-1]
            elif i == "D":
                stack.append( 2 * stack[-1] )
                sum += stack[-1]
            else:
                stack.append(int(i))
                sum += stack[-1]
                
        return sum