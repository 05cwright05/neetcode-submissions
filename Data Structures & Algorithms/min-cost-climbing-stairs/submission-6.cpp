class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int prev = 0;
        int prev_prev = 0;
        for (int i = 2; i <= cost.size(); i++) {
            int curr = 0;
            curr = min(prev+cost[i-1], prev_prev+cost[i-2]);
            prev_prev = prev;
            prev = curr;
        }
        return prev;
    }
};
