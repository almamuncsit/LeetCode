from collections import deque


class MyQueue:
    def __init__(self):
       self.queue = deque([])

    def push(self, x: int) -> None:
        self.queue.appendleft(x)

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0
