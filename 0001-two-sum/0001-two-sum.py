class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

#since there will always be 2 numbers in the list that add up to target
#that means num2 = target - num
#use a dictionary to keep track of the number value & its index

        dictionary = {}
        for idx, num in enumerate(nums):
            num2 = target - num
            if num2 in dictionary:
                return [dictionary[num2], idx]
            else:
                dictionary[num] = idx
                
#test case:
# nums[0] is 2, 9-2 is 7, 7 is not in dictionary, so we add {2: 0} to it
# dictionary = {2: 0} currently
# nums[1] is 7, 9-7 is 2, 2 IS in dictionary, so we return
# >>>[dictionary[2], our current index]
# [0, 1] which is the answer

    #solution 2
    
#         answer = []

#there's only 1 solution in each list, so we can just use for loops & not have worry about repeats/exit conditions
#dict method stores all until solution, list method only stores solution

#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     answer.append(i)
#                     answer.append(j)
        
#         return answer