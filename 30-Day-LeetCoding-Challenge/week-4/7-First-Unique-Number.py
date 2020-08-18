from typing import List


class Node:
    def __init__(self, val):
        self.data = val
        self.previous = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            node.next.previous = self.head
        self.size += 1

    def delete(self, node):
        if self.head is None:
            return
        elif self.size == 1:
            self.head = self.tail = None
        elif self.head == node:
            self.head = self.head.next
        elif self.tail == node:
            self.tail.previous.next = None
            self.tail = self.tail.previous
        else:
            node.previous.next = node.next
            node.next.previous = node.previous
        self.size -= 1


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.numbers = []
        self.memo = {}
        self.linked_list = LinkedList()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.linked_list.tail:
            return self.linked_list.tail.data
        else:
            return -1

    def add(self, value: int) -> None:
        self.numbers.append(value)
        if value in self.memo:
            self.memo[value][0] += 1
            if self.memo[value][0] == 2:
                self.linked_list.delete(self.memo[value][1])
        else:
            node = Node(value)
            self.linked_list.insert(node)
            self.memo[value] = [1, node]


# Your FirstUnique object will be instantiated and called as such:
nums = [2, 3, 5]
obj = FirstUnique(nums)
print(obj.showFirstUnique())
obj.add(6)
print(obj.showFirstUnique())
obj.add(2)
print(obj.showFirstUnique())
