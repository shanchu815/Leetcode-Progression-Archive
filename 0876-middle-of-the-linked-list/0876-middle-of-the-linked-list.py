# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast = head
        slow = fast
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            
        return slow
    
# since slow moves at 1x speed & fast moves at 2x speed
# fast will always be twice the distance from slow
# so by the time it reaches the end of the list,
# slow will be at the middle of the list
# so we just need to return slow once fast is unable to move
# in example 2, slow gives us 4 because the movement of the
# pointers was like this:
# S: 1, F: 1
# S: 2, F: 3
# S: 3, F: 5
# S: 4, F: NULL (it went past 6), while loop stops here
# so this code will always give us the 2nd middle node of the list

# fast will only point to odd locations since it starts from the first
# node & goes by 2. odd + even = odd number, only even + even or
# odd + odd will give even numbers, but our fast pointer won't ever
# move by an odd number of steps.