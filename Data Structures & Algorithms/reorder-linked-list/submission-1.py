class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # 1) find the middle
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # 2) cut into two pieces：head..prev and slow..end
        prev.next = None  # IMPORTANT: if we don't cut it clearly it may cause cycle

        # 3) reverse the slow...end
        prev2, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev2
            prev2 = curr
            curr = nxt
        second = prev2  # add new tails again

        # 4) zippedly rebuild the answer
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1 if tmp1 else second  
            second = tmp2
