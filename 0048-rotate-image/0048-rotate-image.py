class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        left = 0
        right = len(matrix) - 1
#it's a square so the boundaries of L to R & T to B are the same length
        
        while left < right:
            
#so for the first rotation, it will handle the edges (minus 0 does nothing)
#and the second rotation will handle the inner parts (minus 1 or plus 1)
            for cell in range(right - left):
                top = left
                bottom = right
                
#create a temp value to store the topleft corner
                topLeft = matrix[top][left + cell]    
    
#move the bottom left value into that spot
                matrix[top][left + cell] = matrix[bottom - cell][left]
    
#now keep going
                matrix[bottom - cell][left] = matrix[bottom][right - cell]
                matrix[bottom][right - cell] = matrix[top + cell][right]
        
#now move the saved value into here
                matrix[top + cell][right] = topLeft
    
#shrink the left right boundaries
            left += 1
            right -= 1
        
#so this means we start with range(2-0 aka 2), then range (1-1 aka 0) so it stops there
#leaving the center value un-touched because it has nothing to swap with