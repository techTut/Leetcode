# Definition for singly-linked list.

from heapq import merge


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = current = ListNode(0)
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next  
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        
        current.next = list1 or list2
        return dummy.next



    
if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    merged = s.mergeTwoLists(l1, l2)
    while merged:
        print(merged.val, end= " -> ")
        merged = merged.next
    print("X")