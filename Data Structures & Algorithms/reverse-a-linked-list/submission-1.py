# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # first node will become no next
        prev = None
        curr = head
        if not curr or not curr.next:
            return head
        while curr.next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr.next = prev
        return curr