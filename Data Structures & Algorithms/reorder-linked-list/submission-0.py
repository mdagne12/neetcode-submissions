# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # break the list in the two halves
        front_half = head
        back_half = slow.next
        slow.next = None

        # reverse the second half of the list
        prev = None
        curr = back_half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node 

        back_half = prev
        while front_half and back_half:
            tmp1, tmp2 = front_half.next, back_half.next
            front_half.next = back_half
            back_half.next = tmp1
            front_half, back_half = tmp1, tmp2



