# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        c = head
        p = None
        while c:
            next_node = c.next
            c.next=p
            p=c
            c=next_node
        return p
        