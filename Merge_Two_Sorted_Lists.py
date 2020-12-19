# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Start at the heads of l1 and l2 to see which value is less
        # If one value is less, add to next nodes value
        # Increment the pointer on that linked list and repeat the loop while l1 and l2 exists
        # At end of loop, add whatever's left to output
        # Base cases - if l1 doesn't exist, return l2 (no linked list on l1 -> return l2)
        if not l1: return l2
        # if no l2 => return l1
        if not l2: return l1
        current = dummy = ListNode(0) # dummy node
        # create loop 
        while l1 and l2:
            #check to see if l1's value < l2
            if l1.val < l2.val:
                #Add to current next node
                current.next = l1
                #Increment l1 pointer   
                l1 = l1.next
                #otherwise, do the opposite
            else:
                current.next = l2
                l2=l2.next
                # make sure current pointer is incremented
            current = current.next
        # Add rest of l1 & l2 depending on what remains
        if l1: current.next = l1
        if l2: current.next = l2
        
        return dummy.next