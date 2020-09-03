package main

import "fmt"

// TreeNode Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	if p == nil || q == nil {
		return false
	}
	if p.Val != q.Val {
		return false
	}

	return isSameTree(p.Right, q.Right) && isSameTree(p.Left, q.Left)
}

func main() {
	two := TreeNode{4, nil, nil}
	three := TreeNode{3, nil, nil}
	one := TreeNode{1, &two, &three}

	two1 := TreeNode{4, nil, nil}
	three1 := TreeNode{3, nil, nil}
	one1 := TreeNode{1, &two1, &three1}

	fmt.Println(isSameTree(&one, &one1))
}
