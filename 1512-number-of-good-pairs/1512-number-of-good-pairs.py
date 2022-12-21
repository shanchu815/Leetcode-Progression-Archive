class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        
        n = len(nums)
        good_pairs = 0
        
        for i in range(n-1):
            for j in range(1, n):
                
                if nums[i] == nums[j] and i < j:
                    good_pairs += 1
                    
                    
        return good_pairs