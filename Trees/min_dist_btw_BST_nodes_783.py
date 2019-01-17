"""
Given a Binary Search Tree (BST) with the root node root, 
return the minimum difference between the values of any two different nodes in the tree.

Runtime: 52 ms, faster than 96.30% of Python3 online submissions for Minimum Distance Between BST Nodes.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def walk_inorder(root, elements):
            if root:
                walk_inorder(root.left, elements)
                elements.append(root.val)
                walk_inorder(root.right, elements)
        
        bst_elemenets = []
        walk_inorder(root, bst_elemenets)
        index = len(bst_elemenets) - 1
        while index > 0:
            bst_elemenets[index] -= bst_elemenets[index-1]
            index -= 1
        return min(bst_elemenets[1:])