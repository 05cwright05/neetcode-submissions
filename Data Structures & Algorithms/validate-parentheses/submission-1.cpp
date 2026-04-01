#include <iostream>
#include <stack>
class Solution {
public:
    bool isValid(string s) {
        std::stack<char> checker;
        for (char c : s) {
            if (c == '[' || c == '(' || c == '{') {
                checker.push(c);
            } else {
                if (checker.empty()) {
                    return false;
                }
                if (checker.top() == '[' && c != ']') return false;                if (checker.top() == '[' && c != ']') return false;
                if (checker.top() == '{' && c != '}') return false;
                if (checker.top() == '(' && c != ')') return false;
                checker.pop();
            }
        }
        if (!checker.empty()) {
            return false;
        }
        return true;
    }
};
