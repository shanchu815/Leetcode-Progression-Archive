class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        count = {}
        dupes = []
        
        for num in nums:
            if num in count:
                dupes.append(num)
                
            count[num] = 1
        
        return dupes
    
    # use a dictionary to keep track of dupe #s
    # they only appear 1x or 2x, so no need to increase
    # its count to 2, just save the first occurences
    # in the dictionary & save the second occurence in the list