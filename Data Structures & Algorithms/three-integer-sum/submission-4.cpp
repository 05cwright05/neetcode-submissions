class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        //optimize the bih
        //maybe we can run 2 sum to get all possible sums and then search for compliemnts
        //likethe other way
        // like we take the first number of the array
        // the we perform 2 sum to find its compliment in the rest

        vector<vector<int>> result;

        for (int i = 0; i < nums.size(); ++i) {
            int curr = nums[i];
            int target = -curr; //find the compliment
            unordered_set<int> dict;
            for (int j = 0; j < nums.size(); j++) {
                if (j==i) continue; //cant reuse i
                //if its compliment of the target is in the dict we found it
                cout << "Target is " << target;
                if (dict.contains(target-nums[j])) {
                    cout<<"HIT with" << curr << " " << nums[j] << " "<< target - nums[j];
                    // we need to sort and see if it contains
                    vector<int> new_jawn = {curr, nums[j],target-nums[j]};
                    sort(new_jawn.begin(), new_jawn.end());
                    bool present = find(result.begin(), result.end(), new_jawn) != result.end();
                    if (!present) result.push_back(new_jawn);
                } else {
                    dict.insert(nums[j]);
                }
            }
        }
        return result;

    }
};
