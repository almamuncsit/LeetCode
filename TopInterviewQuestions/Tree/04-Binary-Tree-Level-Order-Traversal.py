# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.output = []


    def traverse(self, order, node):
        if order < len(self.output):
            self.output[order].append(node.val)
        else:
            self.output.insert(order, [node.val])

        if node.left:
            self.traverse(order+1, node.left)

        if node.right:
            self.traverse(order+1, node.right)


    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        self.traverse(0, root)

        return self.output
