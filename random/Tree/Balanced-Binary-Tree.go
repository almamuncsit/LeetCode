// TreeNode Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isBalanced(root *TreeNode) bool {
	ans := true
	heightTraverse(&ans, root)

	return ans
}

func heightTraverse(ans *bool, node *TreeNode) int {
	if node == nil {
		return 0
	}

	lh := heightTraverse(ans, node.Left) + 1
	rh := heightTraverse(ans, node.Right) + 1

	*ans = *ans && (lh == rh || lh+1 == rh || lh == rh+1)

	if lh > rh {
		return lh
	} else {
		return rh
	}
}