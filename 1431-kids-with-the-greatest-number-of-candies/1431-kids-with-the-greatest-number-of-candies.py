class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        new_candies = [(x + extraCandies) for x in candies]
        max_candy = max(candies)
        boolist = []
        
        for candy in new_candies:
            
            if candy >= max_candy:
                boolist.append(True)
                
            else:
                boolist.append(False)
                
                
        return boolist
            