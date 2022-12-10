class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        return sum(list(range(len(nums) + 1))) - sum(nums)
    
    # the correct list would have #s from 0 to n
    # with n being the length of our given list
    # & our given list consists of unique #s
    # so we just need to get the sum of that list
    # making sure to increase it by 1 to include
    # n itself in the total sum
    # & then we subtract the sum of our given list
    # from it & it will give us our missing #