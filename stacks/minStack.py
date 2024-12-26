class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.minStack) != 0:
            top = self.minStack[-1]
        else:
            top = val
        self.minStack.append(min(top, val))
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()
        self.minStack.pop()
        print(self.stack)
        

    def top(self) -> int:
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minStack) == 0:
            return -1
        return self.minStack[-1]
