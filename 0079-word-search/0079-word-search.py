class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        
        path = set() #set so we dont reuse previous coordinates
        
        # helper function to check validity, pos = length of our current word
        def dfs(row, column, pos):
            
            if pos == len(word): # our word path matches the target word!
                return True
            
            if (row < 0 or column < 0 or row >= rows or column >= cols or 
            word[pos] != board[row][column] or 
            (row, column) in path):
                return False
                
            # line 14 - out of bounds, incorrect letter found or letter already used
            
            path.add((row, column)) # letter found, add the coordinates
            
            result = (dfs(row + 1, column, pos + 1) # North
                      or dfs(row - 1, column, pos + 1) # South
                      or dfs(row, column + 1, pos + 1) # East
                      or dfs(row, column - 1, pos + 1)) # West
            
            path.remove((row, column)) # no longer need to visit these coordinates
            
            return result

        # pos has to start at 0
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
                
        return False