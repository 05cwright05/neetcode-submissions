class Solution {
public:
    int climbStairs(int n) {
        // so solution one is brute force, now all i need to make it faster is to remember the previous step instead of recursing all the way down
        vector<int> dp;
        dp.push_back(0);
        dp.push_back(1);
        dp.push_back(2);
        for (int i = 3; i <= n; i++) {
            dp.push_back(dp[i-1] + dp[i-2]);
        }
        return dp[n];
    }
};
