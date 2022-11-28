class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
             
        res = []
        
        prod = 1
        for num in nums:
            res.append(prod)
            prod *= num

        prod = 1
        for i in range(len(nums) - 1, -1, -1): #i = [3, 2, 1, 0]
            res[i] *= prod
            prod *= nums[i]
            
        return res
    
    #[a, b, c, d] -> [bcd, acd, abd, abc]
    
    #res = [1], prod = 1*a
    #res = [1, a], prod = a*b
    #res = [1, a, ab], prod = a*b*c
    #res = [1, a, ab, abc] prod = a*b*c*d
    
    #we need to
    #change 1 to bcd, change a to acd, change ab to abd & do nothing to abc
    #prod reset to 1 because abc * 1 = abc
    
    #i = 3, res = [1, a, ab, abc], prod = 1 * d
    #i = 2, res = [1, a, abd, abc], prod = c * d 
    #i = 1, res = [1, adc, abd, abc], prod = b * c * d
    #i = 0, res = [bcd, adc, abd, abc], prod = a * b * c * d