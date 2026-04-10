class ListNode:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.val = value
        self.key = key

class LRUCache:
    # need to support get which returns a key if it exists or a -`
    # likely will need some kind of hashmap to accomplush this in O(1)

    # support put which puts a key in in O(1) or updates it (again will need to refernce a hashmap)

    # key here is that we have a fixed capacity and the  LRU should be ejected when a new one comes  in
    # We couldha ve a tracker for this  but  we  would have to update all hte others
    # we could also potenitally have a linked list where we insert at tail and remove at head
    # head would be least recently and tail would be most recently used
    # if  our current size ever  exceeds the capacity we can just remove wahtever is next to the head
    # to support these we will maek this a doubly linked list

    def moveToBack(self,node):
        # move a node from its current position wherever it is to the back
        prev = node.prev
        next = node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        self.insertNodeAtBack(node)


    def insertNodeAtBack(self, node):
        # insert a node at end of list
        prev_last_node = self.tail.prev
        prev_last_node.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev_last_node
    def deleteLRU(self):
        # delete the first node
        first_node = self.head.next
        next = first_node.next
        if next:
            next.prev = first_node.prev
        print(first_node.key,first_node.val)
        #guranteed to exist since capcity >= 1
        self.head.next = first_node.next
        # delete the entry
        del self.mapping[first_node.key]
    def __init__(self, capacity: int):
        self.capacity = capacity
        # use a dummy head and tail so we dont need to have weird edges cases where our capcity is 1
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mapping = {} # retains key and memory address of node in doubly linked list
        # we dont need to maintain a size varibale cuz we can just use the size held in self.mapping

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        if key in self.mapping:
            node = self.mapping[key]
            self.moveToBack(node)
            return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.mapping[key].val = value
            self.moveToBack(self.mapping[key])
        else:
            new_node = ListNode(key,value)
            self.insertNodeAtBack(new_node)
            self.mapping[key] = new_node

        if len(self.mapping) > self.capacity:
            self.deleteLRU()
