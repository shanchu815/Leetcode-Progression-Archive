class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        letters = [s.lower() for s in licensePlate if s.isalpha()]
        
        for word in sorted(words, key = len): #sorts by length
            check = letters.copy() #need a deep copy here, not a slice
            
            for c in word:
                if c in check:
                    del check[check.index(c)] #gets first occurrence of c
                    
            if len(check) == 0:
                return word

# we sort first to get the shortest words at the beginning
# so theoretically, our for loop can find the correct word faster
# this only works because of how Python's sort works
# so the EARLIEST shortest occurrence of the og list will be at the very front