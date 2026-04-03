# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #general strategy will be to count the number of nodes with a single pass
        #then subtract n from the total number of nodes
        # that is the number of times we will need to leap forward, while finding our target
        # to remove we need to set the prev to the one being deleteds next. 
        # and cleaning the pointers
        
        if not head:
            return None
        c = head
        num_nodes = 0
        while c:
            c = c.next
            num_nodes+=1

        target_node = num_nodes - n # the 0 indexed from beginning node to murder
        if target_node == 0:
            return head.next

        c = head
        p = None
        node_index = 0
        while c:
            if node_index == target_node:
                p.next = c.next
                c.next = None
                return head
            p = c
            c = c.next
            node_index+=1