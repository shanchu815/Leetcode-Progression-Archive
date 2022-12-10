# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        #our absolute mininum starting sum
        curr_max = [root.val]
        
        def dfs(node):
            
            # null node = 0, valid nodes can be + or -
            if not node:
                return 0
            
            
            # left & right values
            Lmax = dfs(node.left)
            Rmax = dfs(node.right)
            
            # check for negative values
            Lmax = max(Lmax, 0)
            Rmax = max(Rmax, 0)
            
            
            # compare our current max sum to our new sum
            # & update it
            curr_max[0] = max(curr_max[0], node.val + Lmax + Rmax)
            
            
            # the sum of the side with the higher sum(s)
            return node.val + max(Lmax, Rmax)
        
        
        dfs(root)
        return curr_max[0]
        