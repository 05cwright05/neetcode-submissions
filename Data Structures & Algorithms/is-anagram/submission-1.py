class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # add the characters of the first string to list
        # then remove for each of the cahracters in the second string
        # if it is not exactly empty at the end return false
        # if we ever dont have the letter we need retrun false

        # we will use a hashmap instead

        letters = {}
        for char in s:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
        
        for char in t:
            if not letters.get(char) or letters[char] <= 0:
                return False
            letters[char] -= 1

        for value in letters.values():
            if value != 0:
                return False
        return True