class Solution {
public:
    int characterReplacement(string s, int k) {
        //store the frequencies so we can ideitnify the most frequent
        unordered_map<char, int> frequencies;
        int left = 0;
        int right = 0;
        int max_size = 0;
        int max_freq = 0;
        while (right < s.size()) {
            frequencies[s[right]]++;
            max_freq = max(max_freq, frequencies[s[right]]);
            while (right-left+1 - max_freq > k) {
                frequencies[s[left]]--;
                left++;
                if (left >= s.size()) {
                    return max_size;
                }
            }
            max_size = max(max_size, right-left+1);
            right++;
        }
        return max_size;
    }
};
