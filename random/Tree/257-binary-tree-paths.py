from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.paths = []

    def traverseWithPath(self, path: str, node: TreeNode):
        if not node.left and not node.right:
            self.paths.append(path)

        if node.left:
            self.traverseWithPath(path + "->" + str(node.left.val), node.left)

        if node.right:
            self.traverseWithPath(
                path + "->" + str(node.right.val), node.right)


    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        self.traverseWithPath(str(root.val), root)

        return self.paths
