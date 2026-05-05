# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy # 基本操作，就是在定義開頭在哪裡
        addone = 0
        while l1 or l2 or addone:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1+val2+addone
            addone = val//10
            val %= 10
            cur.next = ListNode(val) #我們創建一個新的linkedin list從dummy出發，第一個數字舉例來說就是1+4 = 5
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next


        return dummy.next