class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # m = # of rows
        # n = # of columns
        
        if not matrix:
            return []
        
        m = len(matrix) # 3
        n = len(matrix[0]) # 4
        
        first_row_check = False
        first_col_check = False
        
        for r in range(m): # 0 to 2
            for c in range(n): # 0 to 3
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row_check = True
                    if c == 0:
                        first_col_check = True
                        
                    matrix[r][0] = 0 #flag the start of the row
                    matrix[0][c] = 0 #flag the start of the column
                    
        # now we can start our ranges from 1
        # as all the valid starts have been changed to 0
        
        for r in range(1,m):
            for c in range(1,n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    
        # first condition checks for horiz flag
        # sec condition checks for vertical flag
        # cell value is changed if flag is found
                    
        if first_row_check:
            for c in range(n):
                matrix[0][c] = 0
                
        if first_col_check:
            for r in range(m):
                matrix[r][0] = 0
    
    # in ex 1:
    # flags are set at matrix[0][1] & matrix[1][0]
    # the checks are not changed to True
    
    # matrix = [[1,"0",1], "0" means a flagged 0
    #           ["0",0,1],
    #           [1,1,1]]
    
    # r = 1, c = 1
    # matrix[1][1]
    # matrix[0][c aka 1] = 0
    # matrix[r aka 1][0] = 0
    # change matrix[1][1] to 0

    # matrix = [[1,"0",1],
    #          ["0",0*,1], 0* means it was already a 0
    #           [1, 1, 1]]    
    
    # r = 1, c = 2
    # matrix[1][2]
    # matrix[0][2] = 1
    # matrix[1][0] = 0
    # change matrix[1][2] to 0

    # matrix = [[1,"0",1],
    #          ["0",0*,0],
    #           [1, 1, 1]]
    
    # r = 2, c = 1
    # matrix[2][1]
    # matrix[0][1] = 0
    # matrix[2][0] = 1
    # change matrix[2][1] to 0

    # matrix =  [[1,"0",1],
    #           ["0",0*,0],
    #            [1, 0, 1]]
    
    # r = 2, c = 2
    # matrix[2][2]
    # matrix[0][2] = 1
    # matrix[2][0] = 1
    # no change