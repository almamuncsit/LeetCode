class ProductOfNumbers:

    def __init__(self):
        self.numbers = []

    def add(self, num: int) -> None:
        self.numbers.append(num)

    def getProduct(self, k: int) -> int:
        mul = 1
        length = len(self.numbers);
        for x in range(length, length - k, -1):
            mul *= self.numbers[x - 1]
        return mul


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.getProduct(2))
print(obj.getProduct(3))
print(obj.getProduct(4))
