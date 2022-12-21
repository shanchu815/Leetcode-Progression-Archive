class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        new_nums = []
        
        for i in range(len(nums)):
            
            new_num = sum(nums[ : i+1])
            new_nums.append(new_num)
            
            
        return new_nums