# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head

        while fast:
            if fast.val == slow.val:
                fast = fast.next
            else:
                slow = slow.next
                slow.val = fast.val
                fast = fast.next
        
        slow.next =  None
        return head
        


        