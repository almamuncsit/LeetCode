# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: TreeNode) -> int:

        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            if node.val <= lower or node.val >= upper:
                return False
            
            if not helper(node.right, node.val, upper):
                return False

            if not helper(node.left, lower, node.val):
                return False
            
            return True
            
        return helper(root)
        
