class Solution {
public:
    int findMin(vector<int> &nums) {
        //we need to find the index at which the the next item is smaller than the previous
        // the second value in such pair is the min

        int left = 0;
        int right = nums.size() - 1;
        cout << left << ' ' << right << "\n";

        while (left < right) {
            int mid = left + ((right - left) / 2);
            cout << mid << "\n";
            if (nums[mid] >= nums[right]) {
                // the break is to the right
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return nums[left];
    }
};
