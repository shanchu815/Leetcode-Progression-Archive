class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        twoD = []
        
        if m*n == len(original):
            for i in range(0, m*n, n):
                twoD.append(original[i : i + n])
                
        return twoD
    
    # original array needs to be a multiple of m & n to work
    # m x n is the end of the range since it's the size of the 2d array
    # n would be the interval since it's the # of columns
    # a row is automatically created by line 7
    # the row would have to be [i : i + n] & not [i : n] since we start 
    # at idx 0 for i
    # then it would jump to n, 2n, 3n & so on, until it goes out of bounds
    # so the rows would be [0 : n], [n : 2n], [2n : 3n], ..., [(m-1) * n : m * n]