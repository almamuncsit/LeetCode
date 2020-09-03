package main

// ListNode Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	node := head

	for node != nil {
		if node.Next == nil {
			return head
		}
		if node.Val == node.Next.Val {
			node.Next = node.Next.Next
		} else {
			node = node.Next
		}
	}

	return head
}

func main() {

}
