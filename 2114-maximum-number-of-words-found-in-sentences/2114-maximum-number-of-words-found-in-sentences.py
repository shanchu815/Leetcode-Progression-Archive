class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        max_words = 0
        
        for sentence in sentences:
            w = sentence.split(" ")
            max_words = max(max_words, len(w))

        
        return max_words