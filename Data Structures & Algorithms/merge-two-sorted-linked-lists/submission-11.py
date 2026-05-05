# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            head = ListNode(val=list2.val, next=None)
            list2 = list2.next
        elif not list2:
            head= ListNode(val=list1.val, next=None)
            list1 = list1.next 
        elif list1.val <= list2.val:
            head = ListNode(val=list1.val, next=None)
            list1 = list1.next
        else:
            head = ListNode(val=list2.val,next=None)
            list2 = list2.next
        answer = head
        print(answer)
        while list1 or list2:
            if not list1:
                newnode= ListNode(val=list2.val, next=None)
                head.next = newnode
                list2 = list2.next
            elif not list2:
                newnode= ListNode(val=list1.val, next=None)
                head.next = newnode
                list1 = list1.next 
            elif list1.val <= list2.val:
                newnode= ListNode(val=list1.val, next=None)
                head.next = newnode
                list1 = list1.next
            else:
                newnode= ListNode(val=list2.val, next=None)
                head.next = newnode
                list2 = list2.next
            head = head.next
        return answer

                

