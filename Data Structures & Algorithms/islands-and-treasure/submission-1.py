class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Goal is to modify the graph in place such that every INF
        # is replaced with its respective distance to a 0, we cannot traverse -1 (water)
        # Naive solution: For each land chest we should perform breadthfirst search for distance to nearest treasure
        # Slightly better: perhaps we could start breadthfirst search from each of the chests simultaneously and whenever we hit land replace it with the distance
        # ooo that shit is good.

        # lets start by setting up basic breadthfirst search
        # we track the 0 so that we remember our distance
        q = deque()
        visited = [False for _ in range(0,len(grid)*len(grid[0]))]
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] == 0:
                    q.append([row, col, 0])

        while q:
            curr = q.popleft()
            row = curr[0]
            col = curr[1]
            visited[row*len(grid[0]) + col] = True

            distance = curr[2]
            value = grid[row][col]

            if value == 2147483647:
                grid[row][col] = distance
            
            for i in range(0,4):
                nr = row + dx[i]
                nc = col + dy[i]

                if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]):
                    if grid[nr][nc] != -1 and visited[nr*len(grid[0]) + nc] == False: #cant include water #cant revisit
                        q.append([nr,nc, distance+1])
        

