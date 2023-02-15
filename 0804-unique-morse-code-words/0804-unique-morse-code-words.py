class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {"a": ".-","b": "-...","c": "-.-.","d": "-..","e": ".","f": "..-.","g": "--.","h": "....","i": "..","j": ".---","k": "-.-","l": ".-..","m": "--","n": "-.","o": "---","p": ".--.","q": "--.-","r": ".-.","s": "...","t": "-","u": "..-","v": "...-","w": ".--","x": "-..-","y": "-.--","z": "--.."}
        transform = set()
        
        for word in words:
            
            new_w = ""
            
            for i in range(len(word)):
                new_w += morse[word[i]]
            
            transform.add(new_w)
            
        return len(transform)
    
# we translate the words to their morse form and add them to a set
# iterate through each word, get the morse value from our dictionary
# append it to our new_w (new word) string
# and we add it to our set
# and we just have to return the set's length since it only contains unique strings