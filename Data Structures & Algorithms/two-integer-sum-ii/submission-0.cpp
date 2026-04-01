class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        //sicne it is sorted we can do a 2 pointer approach in linear time
        int left = 0;
        int right = numbers.size()-1;

        while(left < right) {
            if ((numbers[left] + numbers[right]) == target) return {left+1,right+1};//add the one as we expect 1 indexed
            else if ((numbers[left] + numbers[right]) < target) left++;
            else right--;
        }
         // should never happen as we are promissed solution
    }
};
