class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int row_size = grid.size();
        int col_size = grid[0].size();
        cout << "row size is " << row_size << "col size is " << col_size << "\n";
        int best_area = 0;

        int dx[] = {-1, 1, 0, 0};
        int dy[] = {0,0,-1,1};

        for (int i = 0; i < row_size; i++) {
            for (int j = 0; j < col_size; j++) {
                
                if (grid[i][j] == 1) {
                    // we are at an island we need to traverse it to get its size
                    queue<pair<int,int>> q;
                    q.push({i,j});
                    cout << "i is " << i << "& j is " << j;
                    int curr_size = 0;

                    while(!q.empty()) {
                        auto [r,c] = q.front();
                        cout << "THE FIRST r of chirsmas " << r << "\n";
                        q.pop();
                        if (r >= 0 && r < row_size && c >= 0 && c < col_size && grid[r][c] == 1) {
                            curr_size++;
                            grid[r][c] = 0;
                            for (int z = 0; z < 4; z++) {
                                int new_r = r + dx[z];
                                int new_c = c + dy[z];
                                q.push({new_r, new_c});
                            }
                        }
                    }
                    best_area = max(best_area, curr_size);
                    
                }
                
            }
        }
        return best_area;
    }
};
