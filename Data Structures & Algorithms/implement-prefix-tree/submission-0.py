class TrieNode:
    def __init__(self, char):
        self.children = {}
        self.char = None
        self.end_of_word = False

class PrefixTree:

    # so basically need some kind of tree where each node can have up to 25 children those being the other possible letters

    # then we can just have branches from those letters

    # thus in the worse case insertion is O(chars in word)

    # retrieval is O(chars in word)

    # can use a set instead of a list to get O(1) retrieval * chars in word


 
    def __init__(self):
        self.sentinel = TrieNode(None)
        

    def insert(self, word: str) -> None:
        curr_node = self.sentinel
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] =TrieNode(char)
            curr_node = curr_node.children[char]
        curr_node.end_of_word = True

    def search(self, word: str) -> bool:
        curr_node = self.sentinel
        for char in word:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        if not curr_node.end_of_word:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.sentinel
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        return True
        