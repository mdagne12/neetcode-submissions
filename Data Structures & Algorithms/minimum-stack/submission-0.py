class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_prefix = []
        

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if (not self.min_prefix) or val < self.min_prefix[-1]:
            self.min_prefix.append(val)
        else:
            self.min_prefix.append(self.min_prefix[-1])
        
    def pop(self) -> None:
        self.main_stack.pop()
        self.min_prefix.pop()
        

    def top(self) -> int:
        return self.main_stack[-1]
        

    def getMin(self) -> int:
        return self.min_prefix[-1]
              
