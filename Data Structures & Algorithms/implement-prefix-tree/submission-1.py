class Node:
    def __init__(self, val):
        self.children = {} # val -> Node
        self.val = val

class PrefixTree:
    """ 
    So the prefix tree must be O(num characters)
    for each operation

    So to do this we should have each character be a node and traverse what we already have at each step
    and only make new stuff when needed

    Basically i could have a head node

    Null
    THen a set of children which could be any of the 26 lettres or $ representing end of string
    We can use this sicne the stirngs are only lower case

    For search isimply traverse


    """
    def __init__(self):
        self.root = Node("$")
        

    def insert(self, word: str) -> None:
        curr = self.root
        word += "$"
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
            



    def search(self, word: str) -> bool:
        curr = self.root
        word += "$"
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return True