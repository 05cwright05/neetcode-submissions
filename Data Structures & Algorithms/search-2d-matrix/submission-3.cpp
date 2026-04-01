class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int left = 0;
        int right = matrix.size() * matrix[0].size() - 1;

        while (left <= right) {
            int mid = left + ((right - left)  / 2);
            int row = mid / matrix[0].size();
            int column = mid % matrix[0].size();
            if (target == matrix[row][column]) return true;
            if (target < matrix[row][column]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return false;
    }
};
