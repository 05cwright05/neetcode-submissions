# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # alright so i assume we need k pointers
        # one at the beginning of each list 
        # at each step we will need to look at all of the next nodes
        # and point the previous to the smallest option
        prev = None
        head = None
        while True:
            min_value = 999999
            min_index = -1

            for i in range(0, len(lists)):
                if not lists[i]:
                    continue
                if lists[i].val < min_value:
                    min_value = lists[i].val
                    min_index = i
            if min_index == -1:
                #implies they are all none
                return head 
            if prev:
                prev.next = lists[min_index]
            else:
                head = lists[min_index]
            prev = lists[min_index]
            lists[min_index] = lists[min_index].next