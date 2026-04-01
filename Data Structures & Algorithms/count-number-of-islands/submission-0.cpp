class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        // the general strategy here is to iterate through all elements in the grid
        // and each time we find a 1 we should increment our number of islands counter
        // Then perform a bfs or dfs from that 1 to all other reachable 1s. Those 1s should be turned into 0s
        // so that they are not recounted later

        int num_islands = 0;

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if (grid[i][j] == '1') {
                    num_islands++;
                    //perform a bfs 
                    int dr[] = {-1, 1, 0, 0};
                    int dc[] = {0, 0, -1, 1};
                    std::queue<std::pair<int,int>> q;
                    q.push({i,j});
                    grid[i][j] = 0;
                    
                    while (!q.empty()) {
                        auto [r,c] = q.front();
                        q.pop();

                        for (int i = 0; i < 4; i++) {
                            int new_row = r + dr[i];
                            int new_col = c + dc[i];

                            // if it is a 1 within the borders we need to change it to a 1 and consider its neighbors, if it is not a 1 we do not need to consider its neighbors
                            // that is we will not add it to the queue
                            if (new_row >= 0 && new_row < grid.size() && 
                                new_col >= 0 && new_col < grid[0].size() && 
                                grid[new_row][new_col] == '1') {
                                
                                grid[new_row][new_col] = '0';
                                q.push({new_row, new_col});
                            }
                        }
                    }
                    
                }
            }
        }
        return num_islands;
    }
};
