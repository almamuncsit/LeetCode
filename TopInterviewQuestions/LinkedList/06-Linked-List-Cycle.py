# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        node = head
        next_node = head.next.next

        while next_node:
            if node == next_node:
                return True

            node = node.next
            
            if next_node.next:
                next_node = next_node.next.next
            else:
                return False

        return False
