class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        //we could return multiple so we lowkey need to check each just in the most efficient way possible
        // though maybe there is a way to shortcut this
        // lets start with brute force
        vector<vector<int>> result;
        for(int x = 0; x < nums.size(); x++) {
            for (int y = x+1; y < nums.size(); y++) {
                for (int z = y+1; z < nums.size(); z++) {
                    if (nums[x]+nums[y]+nums[z] == 0) {
                        // we need to sort and see if it contains
                        vector<int> new_jawn = {nums[x],nums[y],nums[z]};
                        sort(new_jawn.begin(), new_jawn.end());
                        bool present = find(result.begin(), result.end(), new_jawn) != result.end();
                        if (!present) result.push_back(new_jawn);
                    }
                }
            }
        }
        return result;
    }
};
