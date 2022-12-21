class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        n = 0
        subtract = ["--X", "X--"]
        
        for op in operations:
            if op in subtract:
                n -= 1
                
            else:
                n += 1
                
        return n