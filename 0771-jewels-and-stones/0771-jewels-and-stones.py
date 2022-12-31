class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        
        jwl_type = []
        stone_type = []
        count = 0
        
        for jewel in jewels:
            jwl_type.append(jewel)
            
        for stone in stones:
            stone_type.append(stone)
            
        for i in range(len(jwl_type)):
            
            if jwl_type[i] in stone_type:
                gem = jwl_type[i]
                count += stone_type.count(gem)
                
                
        return count

#we loop through jewel types & NOT stone types so we don't
#unnecessarily loop over jewels we already found