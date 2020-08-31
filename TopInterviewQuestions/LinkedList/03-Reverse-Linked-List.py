# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.reversed_head = None

    def reverse(self, previous, node):
        if node.next:
            self.reverse(node, node.next)

        if not self.reversed_head:
            self.reversed_head = node

        node.next = previous

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        self.reverse(None, head)

        return self.reversed_head
