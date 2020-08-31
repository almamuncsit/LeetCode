# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        head = currnet_node = small_node = None

        while l1 or l2:
            if not l1:
                currnet_node.next = l2
                break
            
            if not l2:
                currnet_node.next = l1
                break

            if l1.val <= l2.val:
                small_node = l1
                l1 = l1.next
            else:
                small_node = l2
                l2 = l2.next
            
            if not currnet_node:
                head = currnet_node = small_node
            else:
                currnet_node.next = small_node
                currnet_node = currnet_node.next
        
        return head
            
