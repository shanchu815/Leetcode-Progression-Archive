class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        
        def backtrack(limit, combo, start):
            
			# answer found
            if limit == 0:
                ans.append(combo.copy())
                
            else:
				# iterate through all possible candidates
                for i in range(start, n+1):
                    
					# add candidate
                    combo.append(i)
                    
					#backtrack
                    backtrack(limit-1, combo, i+1)
                    
					# remove candidate
                    combo.pop()

                    
        backtrack(k, [], 1) #we always start at 1 since no 0 in list
        
        return ans
    
    # n = 4, k = 2, combo = []
    # for i in range(start, n+1) aka range(1,5)
    # combo -> [1]
    # backtrack(1, [1], 2)
    # for i in range(2, 5)
    # combo -> [1,2]
    # k hits 0, so a copy of [1,2] is added to ans
    # it can't continue, so combo is popped & become [1] again
    # range(3, 5), range (4, 5), etc.
    