class Solution:
    def countSubstrings(self, s: str) -> int:
        # given a string s
        # return the number of substrings within s that are palindromes
        res = 0
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    res+=1
                else:
                    break
                left -=1
                right+=1

            left = i
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    res+=1
                else:
                    break
                left -=1
                right+=1


            

            # check even length palindromes

        return res