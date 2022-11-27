class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        first = strs[0]
        
        for i in range(len(first)):
            for word in strs:
                if i == len(word) or word[i] != first[i]:
                    return res
                
            res += first[i]
            
        return res
    
    # since we're checking common prefixes, we only need strs[0], the first word, as our limit
    
    # return conditions (no prefix found)
    # i == len(word) means that the index has reached the end of the current word
    # word[i] != strs[0][i] means that the letter in the current word doesn't match the 
    # corresponding letter in the prefix anymore
    
    # prefix found
    # the index is still valid and the letter matches
    # we append that to res
    # when the matches stop, res will not be updated so the return result will have only the 
    # exact matching starting letters