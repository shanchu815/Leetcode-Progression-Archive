# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast = head
        slow = fast
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast: 
                return True
            
            
        return False
    
# the basic 2 pointer for most linked-list questions
# remember that the pointers are separate from the Nodes
# it only stores the memory address of the node
# and is not the node itself
# that's why making fast = fast.next.next doesn't change
# a node's value or position
# slow can just be initialized as fast since they both start
# at the head node

# for 2 pointer method, the fast one moves twice to get to
# the end sooner (if there is one)
# and the slow one moves one node at a time so it will
# hopefully meet up with fast at some point
# don't use more than speed x1 or x2 otherwise you'll get
# errors for short linked lists & whatnot