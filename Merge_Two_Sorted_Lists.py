# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create dummy node so don't have to worry about edge case of inserting into an empty list
        dummy = ListNode(0)
        # tail is normally the dummy
        tail = dummy
        
        # iterate through both lists with while loop
        # If both of them are non-empty, that's when we can compare the two values
        while l1 and l2:
            # do comparison
            if l1.val < l2.val:
                #insert l1 value into tail
                tail.next = l1
                # update l1 pointer
                l1=l1.next
            else:
                    # list 2 is less than or equal. Do exact same thing excecpt use list 2
                tail.next = l2
                    # update l2 pointer
                l2 = l2.next
                # update tail pointer - will be updated regardless of which node we insert into our list
            tail = tail.next
            
            # edge case. What if one of lists is empty but the other is not?
            # find the non-empty list and then insert into the end of our list
            
        if l1: #if l1 is not null
            tail.next = l1
        elif l2: # if l2 is not null
            tail.next = l2
            
        return dummy.next