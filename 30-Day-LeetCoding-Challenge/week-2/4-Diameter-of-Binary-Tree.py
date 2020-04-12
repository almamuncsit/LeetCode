# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.answer = 1

    def diameterOfBinaryTree(self, root):
        self.depth(root)
        return self.answer - 1

    def depth(self, node):
        if not node:
            return 0
        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)
        self.answer = max(self.answer, left_depth + right_depth + 1)
        return max(left_depth, right_depth) + 1
