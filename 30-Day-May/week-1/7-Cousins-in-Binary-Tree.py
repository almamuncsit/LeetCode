# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        cousins = {x: [None, None], y: [None, None]}

        def traverse(parent, node, depth):
            if node.val in cousins and parent:
                cousins[node.val] = [parent.val, depth]
            if node.left:
                traverse(node, node.left, depth + 1)
            if node.right:
                traverse(node, node.right, depth + 1)

        traverse(None, root, 0)
        if cousins[x][0] != cousins[y][0] and cousins[x][1] == cousins[y][1]:
            return True
        else:
            return False


root = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)

root.left = two
root.right = three
two.right = four
three.right = five

sol = Solution()
print(sol.isCousins(root, 4, 5))

