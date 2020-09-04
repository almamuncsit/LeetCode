package main

// TreeNode Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func traverse(output *[][]int, level int, node *TreeNode) {
	if node == nil {
		return
	}

	if level > (len(*output) - 1) {
		*output = append(*output, []int{})
	}

	(*output)[level] = append((*output)[level], node.Val)
	traverse(output, level+1, node.Left)
	traverse(output, level+1, node.Right)
}

func levelOrderBottom(root *TreeNode) [][]int {
	output := make([][]int, 0)
	traverse(&output, 0, root)
	reverse(output)

	return output
}

func reverse(output [][]int) {
	for i, j := 0, len(output)-1; i < j; i, j = i+1, j-1 {
		output[i], output[j] = output[j], output[i]
	}
}
