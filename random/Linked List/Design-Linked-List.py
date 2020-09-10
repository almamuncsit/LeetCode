class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        node = self.head
        for _ in range(index):
            if not node:
                return -1
            node = node.next
        if node:
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node


    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node


    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)

        node = self.head
        for _ in range(index-1):
            if not node:
                return None
            node = node.next
        
        if not node:
            return None

        if node == self.tail:
            return self.addAtTail(val)
        
        new_node = Node(val)
        new_node.next = node.next
        node.next = new_node


    def print(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            return None

        node = self.head
        for _ in range(index-1):
            if not node:
                return None
            node = node.next

        if not node:
            return None
        
        if node.next:
            node.next = node.next.next
        else:
            node.next = None
            self.tail = node

        if not node.next:
            self.tail = node

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# obj.addAtHead(1)
obj.addAtTail(2)
obj.addAtTail(3)
obj.addAtTail(4)
# obj.addAtIndex(2, 6)
# obj.print()
obj.deleteAtIndex(1)
obj.print()

# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
