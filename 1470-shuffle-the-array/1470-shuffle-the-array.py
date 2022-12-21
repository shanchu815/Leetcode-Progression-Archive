class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        x = nums[0 : n]
        y = nums[n : ]
        
        xy = []
        
        for i in range(n):
            
            xy.append(x[i])
            xy.append(y[i])
            
            
        return xy