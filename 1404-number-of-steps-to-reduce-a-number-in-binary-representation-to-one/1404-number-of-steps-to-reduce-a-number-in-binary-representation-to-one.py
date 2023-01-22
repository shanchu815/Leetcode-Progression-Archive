class Solution:
    def numSteps(self, s: str) -> int:
        
        num_s = int(s, 2)
        steps = 0
        
        while num_s > 1:
            
            if num_s % 2 == 0: #even
                steps += 1
                num_s = num_s // 2

            else: #odd
                steps += 1
                num_s += 1

                
        return steps
    
# to convert binary to decimal value, use int(_, 2)
# by default, int() has a base of 10
# we need to change it to base 2 to make it a binary conversion
# ftr, to change decimal to binary, use bin(_)