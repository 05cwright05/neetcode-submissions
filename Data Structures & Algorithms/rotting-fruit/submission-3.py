class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #run multi source bfs from each of the rotten fruits
        # remember the distance from their source (i.e. this is the maximum time)
        # we can treat empty cells as water in a fire spead problem i.e. we cannot visit

        # to save space we can change them to a 2 instead of marking visited

        q = deque()
        fresh_fruit = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 2:
                    q.append([row, col, 0])
                elif grid[row][col]==1:
                    fresh_fruit += 1
        
        # i think with this libary this means that q is not empty
        dr = [-1,0,1,0]
        dc = [0,-1,0,1]
        longest_time = 0
        while q:
            
            curr = q.popleft()
            row = curr[0]
            col = curr[1]
            value = grid[row][col]
            time = curr[2]
            longest_time=max(time,longest_time)

            for i in range(0,4):
                nr = row + dr[i]
                nc = col + dc[i]

                if nc >= 0 and nr >= 0 and nc < len(grid[0]) and nr < len(grid):
                    # only spread to fruit no to empty spaces or to other rotten fruits
                    if grid[nr][nc]==1:
                        q.append([nr,nc,time+1])
                        grid[nr][nc]=2

                        fresh_fruit-=1
        if fresh_fruit > 0:
            return -1
        return longest_time
