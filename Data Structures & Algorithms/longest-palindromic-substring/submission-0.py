class Solution:
    def longestPalindrome(self, s: str) -> str:
        """

        I know that given a string we can find if it is palindrome in O(n) time
        Additionally i think it will be important to know that given a string xxx is a palindrome
        We can find if xxxxx is a palindrome in a single operation thus saving work
        So in reality we can enumerate through all palindromes in O(n) time by expanding from n locations up to n times


        """
        best_left = None
        best_right = None
        best_length = 0
        for i in range(len(s)):
            left = i
            right = i
            # check for odd length

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if (right - left + 1) > best_length:
                        best_length = right-left+1
                        best_left = left
                        best_right = right
                else:
                    break
                left-=1 
                right+=1


            left = i
            right = i+1
            # check for odd length

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if (right - left) + 1 > best_length:
                        best_length = right-left+1
                        best_left = left
                        best_right = right
                else:
                    break
                left-=1
                right+=1
        return s[best_left:best_right+1]
