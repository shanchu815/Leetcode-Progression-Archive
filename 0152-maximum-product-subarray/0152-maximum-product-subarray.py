class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        result = max(nums)
        current_max = 1
        current_min = 1
        
        
        for number in nums:
            old_max = current_max
            current_max = max((number * current_max), (number * current_min), number)
            current_min = min((number * old_max), (number * current_min), number)
            result = max(current_max, result)
            
        return result
    
# result was initialized as the max of nums instead of 0
# this will cut down on the number of comparisons needed
# our current max & min values have to be initialized at 1
# since they will be multiplied for the comparisons
# we are running 3 comparisons in line 12 & 13:
# product of the number & the current max
# product of the number & the current min
# & finally the number by itself
# we need these comparisons for cases in case either number
# or our current min are negative #s