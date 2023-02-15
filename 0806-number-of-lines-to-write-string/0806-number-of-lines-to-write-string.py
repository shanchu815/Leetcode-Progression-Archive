class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        abc = {}
        for i, char in enumerate("abcdefghijklmnopqrstuvwxyz"):
        	abc[char] = widths[i]
            
        lines = 1
        pix = 0
        
        for i in s:
        	pix += abc[i]
            
        	if pix > 100:
        		lines += 1
        		pix = abc[i]
                
                
        return [lines, pix]
        

# so widths is our alphabet & will always be 26 items
# so we make a dictionary to translate letters to their widths
# lines start at 1 because we can't have 0 lines
# pix is set to dic[i] because we will have to start the next line with that letter
# & thus occupy that many pixels from the start of this new line