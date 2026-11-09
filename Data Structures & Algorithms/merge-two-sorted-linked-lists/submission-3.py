# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        if not list1:
            return list2
        if not list2:
            return list1
        
        l1 = list1
        l2 = list2
        
        
        # insert elements in list 2
        while l1 and l2:
            while l2.next and l2.next.val < l1.val:
                l2= l2.next

            if l2.val <= l1.val:
                t = l2.next
                l2.next = ListNode(l1.val, t)
                l1= l1.next
                l2 = l2.next
            else:
                # t = l2
                # l2 = ListNode(l1.val, t)
                # l1 = l1.next
                
                temp = l2.val
                l2.val = l1.val
                l1 = l1.next
                l2next = l2.next
                l2.next = ListNode(temp, l2next)
                

        return temp2
