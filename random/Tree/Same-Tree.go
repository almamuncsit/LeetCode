package main

import "fmt"

// TreeNode Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	pArr := make([]int, 0)
	qArr := make([]int, 0)
	prefixTraverse(&pArr, p)
	prefixTraverse(&qArr, q)

	if len(pArr) != len(qArr) {
		return false
	}

	for i := 0; i < len(pArr); i++ {
		if pArr[i] != qArr[i] {
			return false
		}
	}

	return true
}

func prefixTraverse(Arr *[]int, p *TreeNode) {
	if p == nil {
		return
	}

	*Arr = append(*Arr, p.Val)

	if p.Left != nil {
		prefixTraverse(Arr, p.Left)
	} else {
		*Arr = append(*Arr, 0)
	}
	if p.Right != nil {
		prefixTraverse(Arr, p.Right)
	} else {
		*Arr = append(*Arr, 0)
	}
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
