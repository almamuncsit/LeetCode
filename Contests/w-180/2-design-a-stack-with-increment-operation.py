class CustomStack():
	"""docstring for CustomStack"""
	def __init__(self, maxSize):
		self.maxSize = maxSize
		self.stack = []
	

	def push(self, x: int) -> None:
		if self.maxSize > len(self.stack):
			self.stack.append(x)


	def pop(self) -> int:
		if len(self.stack) == 0:
			return -1

		return self.stack.pop()


	def increment(self, k: int, val: int) -> None:
		n = min(k, len(self.stack))
		for x in range(n):
			self.stack[x] += val


customStack = CustomStack(3)
customStack.push(1)
customStack.push(2)
print(customStack.stack)
customStack.pop()
print(customStack.stack)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.stack)
customStack.increment(5, 100)
customStack.increment(2, 100)
print(customStack.stack)
customStack.pop()
customStack.pop()
customStack.pop()
customStack.pop()
print(customStack.stack)