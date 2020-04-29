# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.maxPath = None

    def maxPathSum(self, root: TreeNode) -> int:
        self.findMax(root)
        return self.maxPath

    def findMax(self, root: TreeNode):
        if root is None:
            return 0
        left_sum = max(self.findMax(root.left), 0)
        right_sum = max(self.findMax(root.right), 0)
        current_sum = root.val + left_sum + right_sum
        max_path = max(left_sum, right_sum, 0)
        if self.maxPath is None or current_sum > self.maxPath:
            self.maxPath = current_sum

        return max_path + root.val


sol = Solution()
root = TreeNode(1)
# two = TreeNode(2)
# three = TreeNode(3)
# four = TreeNode(14)
# five = TreeNode(1)
# root.left = two
# root.right = three
# two.left = four
# two.right = five
print(sol.maxPathSum(root))
# print(sol.maxPath)
