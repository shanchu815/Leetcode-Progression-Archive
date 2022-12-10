class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        all_nums = [x for x in range(1, len(nums) + 1)]
        missing = set(all_nums) - set(nums)
        
        return list(missing)  
    
    # since we're trying to find the #s that are missing
    # from the full range of 1 to n
    # we just need to make a list of #s from 1 to n
    # & then subtract our given list from it
    # our given list can have repeated #s
    # so we turn both lists into sets first & then change 
    # the remainder back into a list