# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        next_node = head
        previous_node = None

        for _ in range(n-1):
            next_node = next_node.next

        while next_node.next:
            next_node = next_node.next
            previous_node = node
            node = node.next

        if head == node:
            head = head.next
        else:
            previous_node.next = node.next

        return head
