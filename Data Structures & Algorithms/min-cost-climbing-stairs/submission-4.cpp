class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> dp(cost.size()+1);
        dp[0] = 0; // We get to start for free
        dp[1] = 0; // we get to start here for free as well

        for (int i = 2; i <= cost.size(); i++) {
           dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]);
        }
        return dp[cost.size()];
    }
};
