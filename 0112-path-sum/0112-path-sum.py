# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
            if not root:
                return False
            
            stack = [(root, root.val)]
            
            while stack:
                currNode, currSum = stack.pop()
                
                #out of nodes & have hit the target sum
                if not currNode.left and not currNode.right and currSum == targetSum:
                    return True
            
                else:
                    if currNode.left: #add all of the left side first
                        stack.append((currNode.left, currSum + currNode.left.val))
                        
                    if currNode.right:
                        stack.append((currNode.right, currSum + currNode.right.val))
                 
                
            return False