# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
            
        return True
    
# ftr, the slow & fast pointers can be initialized in 1 line
# by making it "slow = fast = head"
# a 4 pointer method with the variables prev & temp

# loop on line 18 runs until slow reaches the end of the LL
## 19 - stores slow's future position as temp
## 20 - slow's NEXT changes to prev
## 21 - prev changes to slow's current position
## 22 - slow's current position changes to temp

## if a LL is A -> B -> C & slow is currently at A:
## temp - points to B
## LL no longer has A -> B, because the -> needs to point to prev
## & prev starts as a Null node
## the LL is now A -> Null     B -> C
## prev is storing slow's address now (A)
## slow now becomes temp, so even tho A & B aren't linked anymore
## we can still continue the loop because we've moved slow to B
## temp - C, slow.next = prev results in B -> A -> Null     C
## prev stores (B) & slow changes to C
## since Nll nodes are at the end of a LL, this means that this loop
## has reversed the LL, which is ideal for checking for palindromes

# loop on line 24, prev should have become the head of the reversed LL
## so now we just check if prev & head are the same or not
## this is because we never changed the position of head directly
## we only changed the positions of fast, slow, temp & prev
## so we now have prev, a reversed LL & head, the og LL