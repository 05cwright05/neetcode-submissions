class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;
        int best_volume = 0;
        
        while (left<=right) {
            int curr_vol = min(heights[right], heights[left]) * (right - left);
            if (curr_vol > best_volume) {
                best_volume = curr_vol;
            }
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }
        return best_volume;
    }
};
