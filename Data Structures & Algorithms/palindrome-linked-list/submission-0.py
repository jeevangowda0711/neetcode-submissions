# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the middle half
        # slow will be at half mark
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # compare the first half and second half
        # prev will be the head of the reversed second half
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True