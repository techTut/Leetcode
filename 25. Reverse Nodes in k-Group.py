# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        for i in range(k):
            if not current:
                return head
            
            current = current.next
        
        prev = self.reverseKGroup(current, k)
        
        for i in range(k):
            nextHead = head.next
            head.next = prev
            prev = head
            head = nextHead
        return prev
    