class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        r1 = {"q","w","e","r","t","y","u","i","o","p"}
        r2 = {"a","s","d","f","g","h","j","k","l"}
        r3 = {"z","x","c","v","b","n","m"}
        
        res = []
        
        for word in words:
            l_word = list(word.lower())
            
            if set(l_word).issubset(r1) or set(l_word).issubset(r2) or set(l_word).issubset(r3):
                res.append(word)
                
        return res