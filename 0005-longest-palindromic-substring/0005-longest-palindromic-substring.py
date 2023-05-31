class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        result = ""
        result_length = 0
        
        pal_L_idx = 0
        pal_R_idx = 0
        

        for idx in range(len(s)):
            # odd length palindromes            
            left = idx
            right = idx

            # only runs if valid odd-length palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                
                # (+1) b/c our Left end index isn't inclusive
                if (right - left + 1) > result_length:
                    pal_L_idx = left
                    pal_R_idx = right + 1
                    result_length = (right - left + 1)
                
                left -= 1
                right += 1
            
            # even length palindromes
            left = idx
            right = idx + 1
            
            # only runs if valid even-length palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                
                # (+1) b/c our Left end index isn't inclusive
                if (right - left + 1) > result_length:
                    pal_L_idx = left
                    pal_R_idx = right + 1
                    result_length = (right - left + 1)
                
                left -= 1
                right += 1
                
        # slice once here to save memory space
        result = s[pal_L_idx:pal_R_idx]
        return result
    
# our major difference between the 2 while loops is that to check for
# even length palindromes, we need to set our right index +1