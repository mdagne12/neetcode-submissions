# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        curr = dummy 
        carry_over = 0

        while l1 and l2:
            remainder = (carry_over + l1.val + l2.val) % 10
            carry_over = (carry_over + l1.val + l2.val) // 10

            curr.next = ListNode(remainder)
            curr = curr.next
            l1, l2 = l1.next, l2.next

        leftover_list = l1 if l1 != None else l2

        while leftover_list:
            remainder = (carry_over + leftover_list.val) % 10
            carry_over = (carry_over + leftover_list.val) // 10
            curr.next = ListNode(remainder)
            curr, leftover_list = curr.next, leftover_list.next
            
            
        if carry_over != 0:
            curr.next = ListNode(carry_over)

        return dummy.next


