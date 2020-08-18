# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            node = root
            while node:
                if preorder[i] < node.val and node.left is None:
                    node.left = TreeNode(preorder[i])
                    break
                elif preorder[i] < node.val:
                    node = node.left
                elif node.right is None:
                    node.right = TreeNode(preorder[i])
                    break
                else:
                    node = node.right

        return root
