class Solution:
    def romanToInt(self, s: str) -> int:
        translate = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        
        return sum([translate[x] for x in s])
    
        # can also use map(lambda x: translate[x],s) for the sum's list
        # this is kinda cheating but it's the easiest way (for a person) to think