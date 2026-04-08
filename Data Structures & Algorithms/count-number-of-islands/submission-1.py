class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # first idea is to iterate through the grid
        # when we hit a 1 start a bfs right there and change all the 1s to a 2
        # then iterate to next cell etc. each time we start bfs we up the number of islands by 1
        # the time complexity here is m^2n^2 in the worst case since bfs takes m*n time
        island_count = 0
        dr = [1,0,-1,0]
        dc = [0,1,0,-1]

        def bfs(starting_point):
            q = deque()
            q.append(starting_point)
            while q:
                curr = q.popleft()
                row = curr[0]
                col = curr[1]
                for i in range(0,4):
                    nr = row + dr[i]
                    nc = col + dc[i]
                    if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]):
                        if grid[nr][nc] == "1":
                            q.append([nr, nc])
                            grid[nr][nc] = "2"



        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == "1":
                    island_count +=1
                    grid[row][col] = "2" # mark visited
                    bfs([row, col])
                
        return island_count
