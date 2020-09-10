# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                while head:
                    if head == slow:
                        return head
                    head = head.next
                    slow = slow.next

        return None

one = ListNode(3)
two = ListNode(2)
three = ListNode(0)
four = ListNode(-4)

one.next = two
two.next = three
three.next = four
four.next = None


sol = Solution()
print(sol.detectCycle(one))
