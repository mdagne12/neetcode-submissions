# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front_ptr = back_ptr = head
        
        for i in range(n):
            back_ptr = back_ptr.next

        while back_ptr and back_ptr.next:
            front_ptr = front_ptr.next
            back_ptr = back_ptr.next

        if back_ptr == None:
            return head.next
        else:
            front_ptr.next = front_ptr.next.next
            return head

