# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_node = ListNode()
        tail_node = dummy_node

# tail_node is a separate pointer for our merged list
# we compare list1 & list2's values, adding them
# to our tail pointer & progressing along list1 or list2
# one node at a time
# we progress along the tail at the same speed so we can
# extend it properly
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail_node.next = list1
                list1 = list1.next
                
            else:
                tail_node.next = list2
                list2 = list2.next
                
            tail_node = tail_node.next
        
# if list2 is finished before list1
# add the rest of list1's nodes to tail_node
# remember: list1 & list2 are sorted lists
# so the rest of the nodes are sorted for us

        if list1:
            tail_node.next = list1
                    
# if list1 is finished before list2

        if list2:
            tail_node.next = list2
        
        return dummy_node.next
    
# dummy_node will return a new list starting from the 
# empty node it was initialized with
# so that's why we return dummy_node.NEXT
# we don't return tail_node because it's currently
# located at the end of our new merged list due to our
# while loop & if statements!