# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.total = 0

    def sumation(self, node):
        if node.left:
            if not node.left.left and not node.left.right:
                self.total += node.left.val
            self.sumation(node.left)
        if node.right:
            self.sumation(node.right)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.sumation(root)

        return self.total
