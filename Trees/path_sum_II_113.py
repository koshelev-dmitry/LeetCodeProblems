# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        if root == None:
            return []
        if root.left == None and root.right == None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []

        a = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + i for i in a]

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1           
test_tree = TreeNode(5)
test_tree.left = TreeNode(4)
test_tree.left.left = TreeNode(11)
test_tree.left.left.left = TreeNode(7)
test_tree.left.left.right = TreeNode(2)


test_tree.right = TreeNode(8)
test_tree.right.left = TreeNode(13)
test_tree.right.right = TreeNode(4)
test_tree.right.right.left = TreeNode(5)
test_tree.right.right.right = TreeNode(1)

solution = Solution()
print(solution.pathSum(test_tree, 22))




            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        