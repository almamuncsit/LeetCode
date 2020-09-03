# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.root = None

    
    def insertNode(self, root, node):
        if not root:
            self.root = node
        elif root.val > node.val:
            if not root.left:
                root.left = node
            else:
                self.insertNode(root.left, node)
        elif root.val <= node.val:
            if not root.right:
                root.right = node
            else:
                self.insertNode(root.right, node)
    

    def binary_traverse(self, nums, low, high):
        if low > high:
            return
   
        mid = (low+high)//2
        node = TreeNode(val=nums[mid])
        self.insertNode(self.root, node)
   
        self.binary_traverse(nums, low, mid-1)
        self.binary_traverse(nums, mid+1, high)


    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        self.binary_traverse(nums, 0, len(nums)-1)
        self.pre_order_traverse(self.root)


    def pre_order_traverse(self, node):
        if node.left:
            self.pre_order_traverse(node.left)
        print(node.val)
        if node.right:
            self.pre_order_traverse(node.right)



sol = Solution()
numbers = [1,2,3,4,5,6,7]
sol.sortedArrayToBST(numbers)
