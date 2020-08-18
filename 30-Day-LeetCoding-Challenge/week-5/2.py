# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        n = len(arr) - 1

        def checkPath(i, node):
            if node.val != arr[i]:
                yield False
            elif i == n:
                if node.left is None and node.right is None:
                    yield True
                else:
                    yield False
            elif i < n:
                if node.left and node.left.val == arr[i + 1]:
                    checkPath(i+1, node.left)
                if node.right and node.right.val == arr[i + 1]:
                    checkPath(i+1, node.right)

        result = checkPath(0, root)
        return any(result)
