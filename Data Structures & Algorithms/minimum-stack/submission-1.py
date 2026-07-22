class MinStack:

    def __init__(self):
        self.curr_min = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.curr_min) == 0:
            self.curr_min.append(val)
        else:
            self.curr_min.append(min(val, self.curr_min[-1]))

    def pop(self) -> None:
        self.curr_min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.curr_min[-1]
        
