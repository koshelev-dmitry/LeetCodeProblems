# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0:1}
        
        # recursive to get result
        self.dfs(root, target, 0, cache)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1

# class Solution(object):
    # def pathSum(self, root, sum):
    #     if root == None:
    #         return 0
    #     return (self.pathSumFrom(root, sum) 
    #             + self.pathSum(root.left, sum) 
    #             + self.pathSum(root.right, sum) )
    
    # def pathSumFrom(self, node, sum):
    #     if node == None:
    #         return 0
    #     return (int(node.val == sum) 
    #             + self.pathSumFrom(node.left, sum - node.val)
    #             + self.pathSumFrom(node.right, sum - node.val))


    
    # def pathSum(self, root, target):      
    #     if root == None:
    #         return 0

    #     cache = {1:0} 
    #     self.result = 0
    #     self.dfs_helper(root, target, 0, cache)

    #     return self.result

    # def dfs_helper(self, node, target, pathSum, cache):
    #         if node == None:
    #             return

    #         pathSum += node.val
            
    #         if pathSum == target:
    #             return 1 + calc_paths(node.left, summ, 0) + calc_paths(node.right, summ, 0)
    #         else:
    #             return calc_paths(node.left, summ, pathSum) + calc_paths(node.right, summ, pathSum)
            

# [1,-2,-3,1,3,-2,null,-1] 2
#      1
#    /   \
#  -2    -3
#  /\    /
#  1 3  -2
# /
# -1 
tree = TreeNode(10)

tree.left = TreeNode(5)
tree.right = TreeNode(-3)

tree.left.left = TreeNode(3)
tree.left.right = TreeNode(2)
tree.right.left = None
tree.right.right = TreeNode(-1)

tree.left.left.left = TreeNode(3)
tree.left.left.right = TreeNode(-2)
tree.left.right.right = TreeNode(1)


solution = Solution()
print(solution.pathSum(tree, 1))