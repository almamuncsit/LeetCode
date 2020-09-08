# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = head
        previousNode = None

        while node:
            if node.val == val:
                if previousNode:
                    previousNode.next = node.next
                    node = node.next
                else:
                    head = node.next
                    node = node.next
            else:
                previousNode = node
                node = node.next

        if not previousNode:
            return None
        else:
            return head
