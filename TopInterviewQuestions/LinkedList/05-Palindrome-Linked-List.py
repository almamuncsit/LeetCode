# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __inif__(self):
        self.node = None
        self.ans = True

    def reverse(self, node):
        if node.next:
            self.reverse(node, node.next)
        
        if self.node == node:
            print(True)
        
        node = node.next
        


    def isPalindrome(self, head: ListNode) -> bool:
        self.node = head
        self.reverse(head)
        
