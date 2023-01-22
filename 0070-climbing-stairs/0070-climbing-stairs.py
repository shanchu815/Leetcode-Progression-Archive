class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 2: 
            return n
        
        a, b, curr = 0, 1, 2
        
        while (n > 2):
            a, b = b, curr
            curr = a + b
            n = n - 1
        
        return curr
    
# first if statement is to handle base case of 1 & 2
# this is a fibbonacci style question
# so our inputs -> outputs would be
# 1 -> 1 way, 2 -> 2 ways, 3 -> 3 ways, 4 -> 5 ways
# so basically to get the ways of 3 steps
# we add together the ways of steps 1 & 2
# the same goes for 4 steps
# 1 + 2 = 3, 2 + 3 = 5

# a & b are to store the previous two ways (0 & 1)
# since our n starts at 1, we needed to store the ways for 0 steps
# curr is the ways for n = 2
# so basically (if n is 2):
# sum of climbStairs(n-1), climbStairs(n-2) & climbStairs(n)

# a becomes 1, b becomes 2
# curr becomes 1 + 2 aka 3
# n is decreased
# this first round gives us the ways for n = 3
# a becomes 2, b becomes 3
# curr becomes 2 + 3 aka 5
# n is decreased
# we now have the ways for n = 4
# and so on so forth until n hits less than 2
# at which point we exit because we already stored the ways for n = 2