# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = True, True
        nodeA = headA
        nodeB = headB

        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
            if not nodeA and a:
                nodeA = headB
                a = False
            if not nodeB and b:
                nodeB = headA
                b = False

        return None
