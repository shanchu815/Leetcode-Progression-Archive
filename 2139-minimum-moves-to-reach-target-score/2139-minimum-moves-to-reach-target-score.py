class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        moves = 0

        while maxDoubles > 0 and target > 1:
            
                moves += target % 2
                target = target // 2
                moves += 1
                maxDoubles -= 1
        
        return moves + target - 1
    

# moves += target % 2
# this is to find the remainder if target is odd
# this will get us the min # of times we need to add by 1
# which is either 1 time or 0 times

# target = target // 2
# we're only adding/doubling, so we need the integer half of target
# we've already counted the remainder before
# we then mark down this as a move
# and we decrease the amount of doubling we can do

# maxDoubles will likely hit 0 before target hits 1
# so we return the sum of our moves & what target has been reduced to
# and we subtract 1 because we're trying to get target to 1, not 0
# in EX 1: maxDoubles was 0, so it was 0 + 5 + (_) = 4
# and the only answer to make that work is -1