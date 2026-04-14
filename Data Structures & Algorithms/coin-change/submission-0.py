class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [0 for _ in range(amount+1)]

        dp[0] = 0

        for i in range(1,amount+1):
            # best way to make 1 is 1 ago plus one cent coin 
            # or 2 back plus a 2 cent coin etc.
            min_cost = math.inf
            for coin in coins:
                if i - coin >= 0:
                    if dp[i-coin]!=-1:
                        min_cost = min(dp[i-coin]+1, min_cost) 
            print(min_cost)
            if min_cost == math.inf:
                dp[i] = -1
            else:
                dp[i] = min_cost
        print(dp)
        return dp[-1]

