class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        
        m = len(matrix)
        n = len(matrix[0])
        
        #coordinates increasing
        l = 0 # left ->
        d = 0 # down V

        #coordinates decreasing
        r = n - 1 #right idx 2
        u = m - 1 #up idx 2
        
        while l <= r and d <= u: # has to be <= or >= or it will not get last values

            # l = 0, r = 2, d = 0, u = 2
            for i in range(l, r + 1): #range(0,3) aka 0, 1, 2
                res.append(matrix[d][i]) #1,2,3, going right
            
            d += 1 #d is 1 now, going down

            # l = 0, r = 2, d = 1, u = 2
            for i in range(d, u + 1): #range(1,3) aka 1, 2
                res.append(matrix[i][r]) #6,9, going down
            
            r -= 1 #r is 1 now, right boundary shrinks
            
            #check to make sure not out of bounds
            #the + 1 is to make sure the range's end is valid
            if not d < u + 1 or not l < r + 1:
                break            
           
        #IMPORTANT!!! Line 33 needs to be OR, not AND
        #it will continue after final value if it's AND
        #we just need to stop as soon as 1 pair of boundaries
        #have been reached, NOT both
        
            # l = 0, r = 1, d = 1, u = 2
            for i in range(r, l - 1, -1): #range(1,-1,-1) aka 1, 0
                res.append(matrix[u][i]) #8,7, going left
                
            u -= 1 #u is 1 now, boundary shrinks
            
            # l = 0, r = 1, d = 1, u = 1            
            for i in range(u, d - 1, -1): #range(1,0,-1) aka 1
                res.append(matrix[i][l]) #4, going up
            
            l += 1 #l is 1 now, left boundary shrinks
            # l = 1, r = 1, d = 1, u = 1  
            
        return res
        
        
        #r coordinate, c coordinate
        
        # matrix[0][0], matrix[0][1], matrix[0][2]
        # r is unchanged, c increases until it hits n (0 to n)
        
        # matrix [1][2], matrix [2][2]
        # r increases by 1 until it hits m, c is unchanged (0 to m)
        
        # matrix[2][1], matrix[2][0]
        # c decreases by 1 until 0, r is unchanged (n to 0)
        
        # matrix[1][1]
        # r decreases (0 to m-1 aka 1), c increases (0 to n-1, aka 1)
        
        # the last 2 for loops need the start of the range to be r & u
        # bc when the range is reversed, it becomes the end of that range
        # r & u are kept the same because the start still keeps that inclusiveness
        # end parameters are exclusive but we need to exclude more
        # so we don't repeat values (like 9 & 7)
        # so l & d need to have -1 so when they become starting params,
        # they will skip over those values