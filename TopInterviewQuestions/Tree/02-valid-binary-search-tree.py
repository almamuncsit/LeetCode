# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def __init__(self):
        self.is_valid = True

    def checkValidity(self, side, node: TreeNode):
        if not node:
            return None

        left_value = self.checkValidity(1, node.left)
        right_value = self.checkValidity(2, node.right)

        print(node.val, left_value, right_value)

        if left_value and left_value >= node.val:
            self.is_valid = False
        
        if right_value and  right_value <= node.val:
            self.is_valid = False

        if side == 1:
            return right_value if right_value else node.val
        else:
            return left_value if left_value else node.val


    def isValidBST(self, root: TreeNode) -> bool:
        self.checkValidity(None, root)

        return self.is_valid
