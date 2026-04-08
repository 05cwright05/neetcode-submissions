# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        prev = None
        while l2 or l1:
            if l1 and l2:
                num = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                num = l1.val
                l1 = l1.next
            else:
                num = l2.val
                l2 = l2.next

            num += carry

            actual_num = num % 10
            new_node = ListNode(actual_num, None)
            if head:
                prev.next = new_node
            else:
                head = new_node
            prev = new_node
            if actual_num != num:
                carry = 1
            else:
                carry = 0
        if carry == 1:
            prev.next = ListNode(1, None)
        return head