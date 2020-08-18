class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = 0

    def push(self, x: int) -> None:
        if not self.stack:
            self.current_min = x
        else:
            if x < self.current_min:
                self.current_min = x
        self.stack.append((x, self.current_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.stack:
            self.current_min = self.getMin()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-10)
minStack.push(14)
print(minStack.getMin())
print(minStack.getMin())
minStack.push(-20)
print(minStack.getMin())
print(minStack.getMin())
print(minStack.top())
print(minStack.getMin())
minStack.pop()
minStack.push(10)
minStack.push(-7)
print(minStack.getMin())
minStack.push(-7)
minStack.pop()
print(minStack.top())
print(minStack.getMin())
minStack.pop()
