# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastwalk = head
        try:
            while fastwalk.next.next and head.next:
                fastwalk = fastwalk.next.next
                head = head.next
                if fastwalk == head:
                    return True
            return False
        except:
            return False
         