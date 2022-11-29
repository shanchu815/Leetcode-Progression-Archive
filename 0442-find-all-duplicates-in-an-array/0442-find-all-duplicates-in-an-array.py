class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        dupes = []
        
        for num in nums:
            n = abs(num)
            # idx j is n-1, but we can't save it as we need
            # to save space
            
            if nums[n - 1] < 0: #check if it was tagged
                dupes.append(n) # the true untagged value
                
            nums[n - 1] = -nums[n - 1] # tag it
            
        return dupes
            
        # numbers are from 1 to n
        # no number is 0 or negative
        # list is n numbers long
        # so the idx is 0 to n - 1
        
        # ex = [4,3,2,7,8,2,3,1]
        # result = [2, 3]
        # n = 8, idx is 0 to 7
        # 0-4, 1-3, 2-2, 3-7, 4-8, 5-2, 6-3, 7-1
        # we must use n as an idx
        # use n - 1 (since valid idxs are 0 to 7 but n can be 1 to 8)
        
        # the solution here is to change all single #s
        # to negative versions of themself
        # when num = 4, we use it to get idx 3 (call it j)
        # we check if nums[3] is negative
        # we then change it to negative if it's not
        # also if num is negative, we need to abs(num) to get n
        # since j = n - 1 & we can't use negative idxs
        
        # [4,3,2,-7,8,2,3,1] num = 4, n = 4, j = 3, nums[j] was 7
        # [4,3,-2,-7,8,2,3,1] num = 3, n = 3, j = 2, nums[j] was 2
        # [4,-3,-2,-7,8,2,3,1] num = -2, n = 2, j = 1, nums[j] was 3
        # [4,-3,-2,-7,8,2,-3,1] num = -7, n = 7, j = 6, nums[j] was 3
        # [4,-3,-2,-7,8,2,-3,-1] num = 8, n = 8, j = 7, nums[j] was 1
        # [4,-3,-2,-7,8,2,-3,-1] num = 2, n = 2, j = 1, nums[j] is -3
        # this means we have run into a number that we have checked before
        # abs(nums[6]) == abs(nums[1]), 2 == 2
        # we need to add n aka 2 to our result
        
        # [4,-3,-2,-7,8,2,-3,-1] num = -3, n = 3, j = 2, nums[j] is -2
        # append another n, this time 3
        
        # [4,-3,-2,-7,8,2,-3,-1] num = -1, n = 1, j = 0, nums[j] was 4
        # [-4,-3,-2,-7,8,2,-3,-1] final list
        
        # we have checked idxs 0, 1, 2, 3, 6, 7
        # idxs 1 & 2 were checked twice bc they're where the dupes are
        # the nums are 2 & 3
        # 2 is at idxs 2 & 5, 3 is at idxs 1 & 6
        # 2 - 1 = 1 & 6 - 1 = 5
        # bc of the constraints, they will always lead to each other if you
        # use one of their idxs as a guide
        
        
        
        
        
        
        
        