# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root, min_val=float('-inf'), max_val=float('inf')):
        # if we at the None leaf => we are finished this subtree
        if not root:
            return True
        
        if min_val < root.val < max_val:
                return (self.isValidBST(root.left, min_val, root.val) 
                            and self.isValidBST(root.right, root.val, max_val))
        else: 
            return False
