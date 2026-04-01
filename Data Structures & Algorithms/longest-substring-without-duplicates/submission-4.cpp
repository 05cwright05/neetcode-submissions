class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> letters;
        int left = 0, right = 0, max_length = 0;
        cout << s.size();
        while (right < s.size()) {
            if (letters.contains(s[right])) {
                max_length = max(max_length, (int)letters.size());
                letters.erase(s[left]);
                left++;
            } else {
                letters.insert(s[right]);
                right++;
            }
            //right++;
        }
        max_length = max(max_length, (int)letters.size());

        return max_length;

    }
};
