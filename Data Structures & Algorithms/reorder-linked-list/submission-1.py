# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #starting at the middle of the list we should reverse it
        # then stitch the two halves togehter

        slow = head
        fast = head
        p = None
        print("1")

        while slow and fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next

        # i think we want the later middle one 
        if fast:
            p = slow
            slow = slow.next
        p.next = None

        print("2")

        #slow now points to middle of the list (if its a list of 4 things points to index 2 out of 3)
        # lets reverse this slow half

        p = None
        while slow:
            next_node = slow.next
            slow.next = p
            p = slow
            slow = next_node
        print("3")

        backward = p
        forward = head
        print("made it")

        while backward:
            r1 = backward.next
            r2 = forward.next

            forward.next = backward
            backward.next = r2
            backward = r1
            forward = r2
