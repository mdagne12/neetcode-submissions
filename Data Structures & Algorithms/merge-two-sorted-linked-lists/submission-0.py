# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = None
        new_curr = None

        while list1 and list2:

            if list1.val < list2.val:
                next_node = list1
                list1 = list1.next
            else:
                next_node = list2
                list2 = list2.next

            if not head:
                head = next_node
                new_curr = head
            else:
                new_curr.next = next_node
                new_curr = next_node

        if list1:
            if head:
                new_curr.next = list1
            else:
                head = list1

        if list2:
            if head:
                new_curr.next = list2
            else:
                head = list2
                
        return head



        