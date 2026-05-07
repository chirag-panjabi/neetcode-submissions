class MinStack:
    # got complete hint from solution about how to keep record of minimum at each point
    def __init__(self):
        self.stk = [] # (val,min_at_that_point)
        self.mini = None

    def push(self, val: int) -> None:
        if self.stk:
            self.stk.append((val, min( self.stk[-1][1] , val) ))
        else:
            self.stk.append((val, val))
        return None

    def pop(self) -> None:
        del self.stk[-1]
        if self.stk:
            self.mini = self.stk[-1][1]
        return None

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]

        
