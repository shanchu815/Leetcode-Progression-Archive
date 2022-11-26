class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #lazy solution
        uni_dict = {}
        
        for num in nums:
            if num in uni_dict:
                return num
            else:
                uni_dict[num] = 1
        
        #better 2 pointer solution
#All the integers in nums appear only once except for 
#precisely one integer which appears two or more times.

# best strategy is to used linked list
# since the list is made up of numbers that go up to n
# and n is the length of the list minus 1 (cuz there is a duplicate in nums!)

#that means all the potential values inside of nums are also valid indices!

#so we keep running slow and fast to run loops through nums until we get
#to a point where slow == fast & just return that

        # slow = nums[0]
        # fast = nums[0]

        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break

#slow moves by 1, fast moves by 2
#we first find the index where they intersect at
#the intersection is where the loop ends
#say the intersection is at index 3, with a value of x
#that means that index x is where the loop STARTS
#so if 3 is the break point & nums[3] = 1
#nums[1] is where the loop starts
                
        # slow = nums[0]

#reset slow back to the start
#we already have fast within the cycle, now we'll change its speed
#there's only 2 duplicate numbers, so the cycle is only 2 "nodes" long

        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[fast]
    
        # return fast

#we can also return slow because they will be equal when the loop breaks

        