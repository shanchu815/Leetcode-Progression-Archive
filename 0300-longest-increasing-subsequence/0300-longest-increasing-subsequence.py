class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        # a list of minimum branch counts
        cache = [1] * len(nums)

        # going backwards from the last index
        for index1 in range((len(nums) - 1), -1, -1):
        
            # going backwards from the second to last index      
            for index2 in range((index1 + 1), len(nums)):
        
                # we're checking for increasing values        
                if nums[index1] < nums[index2]:
                    
                    # update our branch counts
                    cache[index1] = max(cache[index1], (cache[index2] + 1))
    
        return max(cache)
    
# we move backwards through the array & update our cache
# at each index1 with the new current max length
# so at the end of the function, we can simply return the max
# of our cache to get the longest strictly increasing subsequence length