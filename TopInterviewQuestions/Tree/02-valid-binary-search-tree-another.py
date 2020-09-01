# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def __init__(self):
        self.data = []

    def checkValidity(self, node: TreeNode):
        if node.left:
            self.checkValidity(node.left)
        self.data.append(node.val)
        if node.right:
            self.checkValidity(node.right)


    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        self.checkValidity(root)

        for i in range(len(self.data)-1):
            if self.data[i] >= self.data[i+1]:
                return False
        
        return True
