class Node:
    def __init__(self, val):
        self.children = {} # Char -> node
        self.val = val


class WordDictionary:
    """
    Create a data structure that supports adding new words and searching for words

    The twist is that dots can be matched with any letter

    Ok but if we use a traditional prefix trie a . means we would now need to consider either branch
    Like recursively

    Tbh it says this will only happen twice so it may not be that big of a deal




    """
    def __init__(self):
        self.root = Node("$")

    def addWord(self, word: str) -> None:
        word += "$"
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
    def recSearch(self, word, starting) -> bool:
        curr = starting
        for i, char in enumerate(word):
            if char != ".":
                if char not in curr.children:
                    return False
                curr = curr.children[char]
            else:
                for child in curr.children.values():
                    if self.recSearch(word[i+1: len(word)], child):
                        return True
                return False # none of the branches worked
        if curr.val == "$":
            return True
        else:
            return False


    def search(self, word: str) -> bool:
        # ok so when we hit a . we need to call search for each of its children and if any are true retunr true
        word += "$"
        curr = self.root

        return self.recSearch(word, curr)

        
