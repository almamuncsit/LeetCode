
// TreeNode Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func hasPathSum(root *TreeNode, sum int) bool {
	if root == nil {
		return false
	}
	ans := false

	findTotal(root, root.Val, sum, &ans)

	return ans
}

func findTotal(node *TreeNode, total int, sum int, ans *bool) {
	if node.Left == nil && node.Right == nil {
		*ans = *ans || (total == sum)
		return
	}

	if node.Left != nil {
		findTotal(node.Left, total+node.Left.Val, sum, ans)
	}

	if node.Right != nil {
		findTotal(node.Right, total+node.Right.Val, sum, ans)
	}
}