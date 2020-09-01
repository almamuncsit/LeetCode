# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_depth = 0


    def findDepth(self, depth: int, node: TreeNode) -> int:
        self.max_depth = max(depth, self.max_depth)

        if node.left:
            self.findDepth(depth+1, node.left)

        if node.right:
            self.findDepth(depth+1, node.right)


    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.findDepth(1, root)

        return self.max_depth
