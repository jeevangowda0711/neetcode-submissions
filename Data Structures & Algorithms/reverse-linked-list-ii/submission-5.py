# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev = dummy
        current = head

        # get leftPrev and current in position for reversal
        for i in range(left - 1):
            current = current.next
            leftPrev = leftPrev.next
        
        # reverse right - left + 1 nodes
        prev = None
        for i in range(right - left + 1):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        # point leftPrev to the new current 
        leftPrev.next.next = current
        leftPrev.next = prev
    
        return dummy.next