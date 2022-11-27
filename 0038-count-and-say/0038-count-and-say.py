class Solution:
    def countAndSay(self, n: int) -> str:
        
        # n = 1, res = 1, -> "one one"
        # n = 2, res = 11, -> "two ones"
        # n = 3, res = 21, -> "one two, one one"
        # n = 4, res = 1211, -> "one one, one two, two ones"
        # n = 5, res = 111221, -> "three ones, two twos, one one"
        # n = 6, res = 312211, -> "one three, one one, two twos, two ones"
        
        if n == 1:
            return "1"
        
        rec = self.countAndSay(n-1) #using the existing function & calling it recursively
        res = ""
        count = 1
        
        for i in range(len(rec)):
            if i == len(rec) - 1 or rec[i] != rec[i+1]:
                res += str(count) + rec[i]
                count = 1 #reset
                
            else:
                count += 1
        
        return res


# if rec[i] != rec[i+1]
# this is to count the dupe digits
# line 19 isnt triggered because 1 == 1
# & our number is 111221, so count is increased to 3
# line 21 appends the count of the digit (3) & the digit (1)
# so for n = 6, we get [31] for the first part
# then count is reset to 1
# the same thing happens for the 2s

# if i == len(rec) - 1
# this is when we reach the end & have a straggler 1 that has no comparison
# so we have to just append it & the current count (which got reset to 1 earlier) to the end of result
# which becomes [11]