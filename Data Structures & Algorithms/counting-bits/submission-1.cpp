class Solution {
public:
    vector<int> countBits(int n) {
        // brute force
        int bit_mask = 1;
        vector<int> output = {};
        for (int number=0; number <= n; number++) {
            int curr_count = 0;
            bit_mask = 1;
            for (int i = 0; i < 32; i++) {
                if (number & bit_mask) {
                    curr_count++;
                } 
                bit_mask = bit_mask << 1;
            }
            output.push_back(curr_count);
        }
        return output;
    }
};
