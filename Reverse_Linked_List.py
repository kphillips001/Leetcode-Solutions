# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Set previous as None, Current as head, and next as None
# Iterate until Current is None
# Set next node of current to next
# Set previous as current, current as next, and next as its next node
# Head pointer to previous Node
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    
        prev = None
        curr = head
        next = None
    
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev