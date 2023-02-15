class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        indices = {}
        res = []
        idx = 2000
        
        words = set(list1 + list2)
        
        for w in words:
            if w in list1 and w in list2:
                new_sum = list1.index(w) + list2.index(w)
                idx = min(idx, new_sum)
                
                if new_sum in indices:
                    indices[new_sum].append(w)
                    
                else:
                    indices[new_sum] = [w]
                    
        return indices[idx]