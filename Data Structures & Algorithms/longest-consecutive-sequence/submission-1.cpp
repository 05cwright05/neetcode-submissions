class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        int best_sequence = 1;
        int curr_sequence = 1;
        int right = 0;
        int left = 0;

        sort(nums.begin(), nums.end());
        int curr_number = nums[left];

        while (right < nums.size()) {
            right++;
            while(nums[right]==curr_number) {
                right++;
            }
            if (nums[right] == curr_number + 1) {
                curr_number++;
                curr_sequence++;
            } else {
                best_sequence = max(curr_sequence, best_sequence);
                curr_sequence = 1;
                left = right;
                curr_number = nums[left];
            }
        }
        return best_sequence;
    }
};
