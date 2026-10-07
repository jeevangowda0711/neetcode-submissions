class MinStack:

    def __init__(self):
        
        self.minStack = []

    def push(self, val: int) -> None:
        if self.minStack:
            currentMin = min(self.minStack[-1][1], val)
            self.minStack.append((val, currentMin))
        else:
            self.minStack.append((val, val))
        
    def pop(self) -> None:
        self.minStack.pop()
        # if self.minStack:
        #     self.current_min = self.minStack[-1][1]
        # else:
        #     self.current_min = float('inf')

    def top(self) -> int:
        return self.minStack[-1][0]

    def getMin(self) -> int:
        return self.minStack[-1][1]
        
