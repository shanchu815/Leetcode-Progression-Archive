class Solution:
    def minimumSum(self, num: int) -> int:
        
        
        num_list = [int(i) for i in str(num)]
        num_list.sort()
        a = 0
        b = 0
        
        for x in range(4):
            
            if (x % 2) != 0:
                a = a * 10 + num_list[x]
                
            else:
                b = b * 10 + num_list[x]
                
                
        return a + b