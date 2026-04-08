class Solution:
    def climbStairs(self, n: int) -> int:
        # given an integer n return the number of distincy ways to reach the top 
        # The number of ways to reach the second step are the number of ways to reach the previous step +1 or the number of ways to reach
        # the previous previous step

        # so if n i sless than 45 then we could do a 46 long dp_array
        # n+1 long
        # we could say that dp[0] = 0?
        # dp[n] = number of ways to get to prev stair + number of ways to get to prev prev stair + 2 since there are 2 ways to ge to it

        # could do this in linear time then

        # 1 step to get to 1
        # 2 ways to get to 2

        # dp[2] = 2
        # dp[3] = 3
        # dp[4] = 1,1,1,1. 2,2, 1,1,2, 2,1,1 1,2,1

        # so the dp relation is number of ways to reach previous previous step + number of ways to reach prev step
        if n == 1:
            return 1
        if n==2:
            return 2
        dp_array = [0 for _ in range(0,n+1)]

        dp_array[1] = 1
        dp_array[2] = 2

        

        for i in range(3, n+1):
            dp_array[i] = dp_array[i-1] + dp_array[i-2]

        return dp_array[-1]