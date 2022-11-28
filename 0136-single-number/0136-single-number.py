class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        inc_sum = sum(nums)
        n = set(nums)
        total_sum = sum(n) * 2
        
        return total_sum - inc_sum
    
    # since every # appears twice except for one #
    # that means the complete list's sum would be
    # a number that is equal to all the list's unique
    # #s times 2.
    # so we just need to get all the unique #s, double
    # that & compare it to the sum of the original list
    # then it will get the missing #
    
    # ie: list is [a, a, b, b, c]
    # the sum would be 2a + 2b + c
    # corrected list would be [ a, a, b, b, c, c]
    # the sum would be 2a + 2b + c
    # we can get (a, b, c) by changing either list to a set
    
        