class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // so the general idea is we start both at beginning
        // then gradually move right forward
        // if right is ever lower than left move left to where right is
        // kind of a slinky apporach, so we will record the local max for each slinky
        // and decide if our new max is better or not

        int max_profit = 0;
        int left = 0;
        int right = 0;

        while (right < prices.size()) {
            if (prices[right] < prices[left]) {
                left = right;
            } else {
                cout << prices[right] << prices[left] << "\n";
                max_profit = max(max_profit, prices[right] - prices[left]);
            }
            right++;
        }
        return max_profit;
    }


};
