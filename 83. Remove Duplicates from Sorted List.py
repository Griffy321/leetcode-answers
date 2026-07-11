# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy 
        last = None

        while head:
            if last is None or head.val != last:
                last = head.val
                tail.next = ListNode(head.val)
                tail = tail.next
            head = head.next
        return dummy.next