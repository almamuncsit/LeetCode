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

    def delete_last(self):
        if self.head is None:
            return
        elif self.size == 1:
            self.head = self.tail = None
        else:
            self.tail.previous.next = None
            self.tail = self.tail.previous

    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.linked_list = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.linked_list.delete(self.map[key][1])
        self.linked_list.insert(self.map[key][1])
        return self.map[key][0]

    def put(self, key: int, value: int) -> None:
        node = Node(key)
        if key in self.map:
            self.linked_list.delete(self.map[key][1])
            self.linked_list.insert(node)
        else:
            self.linked_list.insert(node)
        self.map[key] = (value, node)

        if len(self.map) > self.capacity:
            del self.map[self.linked_list.tail.data]
            self.linked_list.delete_last()


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(3)
obj.put(2, 1)
obj.put(2, 2)
print(obj.get(2))
obj.put(1, 1)
obj.put(4, 1)

obj.linked_list.print_list()
print(obj.map)
# print(obj.get(2))

# param_1 = obj.get(key)
# obj.put(3, 12)
# obj.put(2, 3)
# obj.put(4, 12)
# obj.put(12, 13)
# obj.linked_list.print_list()
# print(obj.map)
#
# obj.get(4)
# obj.get(2)
# obj.get(4)
# obj.put(5, 50)
# obj.linked_list.print_list()


#
# linked_list = LinkedList()
#
# one = Node(1)
# two = Node(2)
# three = Node(3)
# four = Node(4)
#
# linked_list.insert(one)
# linked_list.insert(two)
# linked_list.insert(three)
# linked_list.insert(four)
# linked_list.print_list()
#
# print('After Delete')
# linked_list.delete_last()
# linked_list.print_list()
