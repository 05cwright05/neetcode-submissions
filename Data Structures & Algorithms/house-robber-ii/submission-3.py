class Solution:
    def rob(self, nums: List[int]) -> int:
        # at each step you can either take the previous value and not rob or take the prev prev and rob
        # ultimaltey that will give us the optimal value so for example 1:
        # suppose we set dp[0] = 3 and d[1] = 4 then for the final house you should take the prev prev and add 3, however,
        # in this case that would not work since we already took the first, so could just have an if check for the very end
        # well if they are a circle you can only rob either the first or the last so we have dp[0] set to max(last house and first )


        # ok i think my simplest idea is to run twice and choose the best answer
        # in the first pass we do normal house_robber but
        # in the second pass 

        # so first pass is normal house robber exlcuding the last house 
        #second pass is normal house robber excluding the first house
        if len(nums) == 2:
            return max(nums[1], nums[0])
        elif len(nums)==1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(dp[0],nums[1])

        for i in range(2, len(nums)-1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        best_value = dp[-2]
        print(best_value)


        dp[0]=0
        dp[1]=nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])


        print(dp[-1])

        return max(best_value, dp[-1])


