class Solution:
    def isValid(self, s: str) -> bool:
        # stack approach that i could think at the moment
        if len(s) % 2 != 0:
            return False
        stack = []

        for br in s:
            stack.append(br)
            if len(stack)>1 and (stack[-2] + stack[-1] in {'{}','[]','()'}):
                del stack[-2:]
                print(stack)
        return stack == []                

