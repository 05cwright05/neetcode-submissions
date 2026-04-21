class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        We should do a db approach starting at the end

        Bascially we know we can break down position length

        From that information we iterate through i backward and at each step if we can add the lgenfth of a word and
        get to the soltuion then we are good
        """

        dp = [False for _ in range(len(s)+1)]
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                # bascially go forward i places and see if its valid
                if i + len(word) <= len(s) and s[i: i+len(word)] == word:
                    # it matches the word
                    # so we can reach the next state
                    dp[i]= dp[i+len(word)]
                    if dp[i]:
                        break

        return dp[0]