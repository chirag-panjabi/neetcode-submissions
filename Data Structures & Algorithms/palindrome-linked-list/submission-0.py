# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        cur = head
        prev = None
        np = cur.next
        slow = head
        fast = head


        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow

        while cur != mid :
            np = cur.next
            cur.next = prev
            # prev.next= None
            prev = cur
            cur = np
        
        if fast:
            mid = mid.next


        while mid and prev:
            if mid.val == prev.val:
                mid = mid.next
                prev = prev.next
            else:
                return False
        return True