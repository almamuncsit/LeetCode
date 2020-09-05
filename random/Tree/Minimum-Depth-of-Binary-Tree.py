# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDepth(self, depth: int, node: TreeNode):
        if not node.left and not node.right:
            self.min_depth = min(self.min_depth, depth)

        if node.left:
            self.findDepth(depth+1, node.left)
        if node.right:
            self.findDepth(depth+1, node.right)


    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.min_depth = float('inf')
        self.findDepth(1, root)

        return self.min_depth
