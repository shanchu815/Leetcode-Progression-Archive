class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        letters = {s[0]}
        L = 0
        R = 1
        idxs = (0, 1)
        
        while R < len(s):
            if s[R] in letters:
                letters.remove(s[L])
                L += 1
                
            else:
                letters.add(s[R])
                R += 1
            
            if R - L > idxs[1] - idxs[0]:
                idxs = (L, R)
                print(idxs)
            
        return idxs[1] - idxs[0]
    
# use a left slider and a right slider
# we initialize our set of letters to check as s[0]
# as we have already cleared the possibility of an empty string

# in the while loop:
# .remove() pops that specific letter
# by using L as the index, we pop from the left of the set
# then we move L to the right by 1
# we keep removing letters & moving right until letters only has
# unique characters in it

# in Ex: 3, our function would look like this:
# L = 0, R = 2, letters = {"p", "w"}, s[R] = "w"
# since "w" is in letters, we pop s[L] aka s[0] aka "p" from it
# now we have {"w"} & L -> 1, but "w" is still in there
# so we pop s[L]. s[L] is "w", so letters becomes an empty set {}
# L is updated to 2
# "w" is now no longer in letters, so we can put that in & update R
# and now we have the following:
# L = 2, R = 3, letters = {"w"}, s[R] = "k"

# the only cases where the function picks up on a substring longer
# than 1 are at (0, 2) & (2, 5). And we get the length 3
# from the 2nd updated version of idxs