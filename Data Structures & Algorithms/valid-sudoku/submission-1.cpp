class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        //lets start with brute force ish, as we go thru a row we will put them in an unorderedset and then check if they are in the set
        //thus time compleixty is just 3n i think technically 

        //print board
        for (int i = 0; i <9; i++) {
            for (int j = 0; j <9;++j) {
                cout << board[i][j] << " ";
            }
            cout << "\n";
        }
        cout << "\n\n\n";
        //for rows

        for (int i = 0; i < 9; i++) {
            unordered_set<int> nums ={};
            for (int j = 0; j < 9; j++) {
                cout << board[i][j] <<"\n";
                if (nums.find(board[i][j]) != nums.end()) {
                    cout << "FAILED COLS" << "\n";
                    return false;
                } else {
                    if (board[i][j] != '.') {
                        nums.insert(board[i][j]);
                    }
                }
            }
        }


        //for cols
        for (int i = 0; i < board.size(); i++) {
            unordered_set<int> nums;
            for (int j = 0; j < board[i].size(); j++) {
                if (nums.find(board[j][i]) != nums.end()) {
                    cout << "FAILED Rows" << "\n";
                    return false;
                } else {
                    if (board[j][i] != '.') nums.insert(board[j][i]);
                }
            }
        }



        //for boxes
        for (int b = 0; b < 9; b++) {
            unordered_set<int> nums;
            for (int i = 3*(b/3); i < 3*(b/3) + 3; i++) {
                for (int j = 3*(b%3); j < 3*(b%3) + 3; j++) {
                    if (nums.find(board[i][j]) != nums.end()) {
                        cout << "FAILED Bixes" << "\n";
                        return false;
                    } else {
                        if (board[i][j] != '.') nums.insert(board[i][j]);
                    }
                }
            }
        }
        return true;
    }
};
