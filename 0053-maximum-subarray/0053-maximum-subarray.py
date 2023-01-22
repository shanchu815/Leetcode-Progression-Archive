class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_max = max(nums)
        curr_sum = 0
        
        for i in range(len(nums)):
            
            if curr_sum + nums[i] < 0:
                curr_sum = 0
                
            else:
                curr_sum = curr_sum + nums[i]
                curr_max = max(curr_sum, curr_max)
                    
                    
        return curr_max
    
# our initial max sum is the max of all the #s in the array
# our current sum is initialized as 0
# so we check if a # in the array would make a negative sum
# & reset curr_sum to 0 if that happens
# if not, then we have a positive sum
# so we save that to curr_sum & then check if it's bigger than our max
# & we set curr_max to the new bigger sum
# & we keep doing this until we run through the whole array