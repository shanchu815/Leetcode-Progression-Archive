class Solution:
    def rob(self, nums: List[int]) -> int:
                
        # first & second houses to rob
        
        rob1 = 0
        rob2 = 0
        
        for house in nums:
            best_loot = max(rob1 + house, rob2)
            # is the loot from list[0]+list[2] better than list[1]?
            
            rob1 = rob2 # slide the array over to the right
            rob2 = best_loot # update the total best loot to be compared
        
        # rob2 will have reached the end of the list first      
        return rob2
    
# line 9: nums will look like:
# [rob1, rob2, house, house+1, ...]
# if we get loot from rob1, the next available loot is from house
# we need to compare if this total loot is better than the loot from rob2
        