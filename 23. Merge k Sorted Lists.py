# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        current = dummy = ListNode(0)
        
        candidate = []
        
        for i, l1 in enumerate(lists):
            if l1:
                heappush(candidate, (l1.val, i, l1))
        
        while candidate:
            value, idx, l1 = heappop(candidate)
            current.next = l1
            current = current.next
            
            l1 = l1.next
            if l1:
                heappush(candidate, (l1.val, idx, l1))
        return dummy.next
    
    