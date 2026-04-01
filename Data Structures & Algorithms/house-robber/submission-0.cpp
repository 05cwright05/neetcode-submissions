class Solution {
public:
    int rob(vector<int>& nums) {
        int prev = 0;
        int prev_prev = 0;

        for (int i = 0; i < nums.size(); i++) {
            int curr = max(prev, prev_prev + nums[i]);
            prev_prev = prev;
            prev = curr;
        }
        return prev;
    }
};
