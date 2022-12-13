class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = nums
        
        ans.extend(nums)
        
        return(ans)
    
    # it's literally just doubling the list so use .extend