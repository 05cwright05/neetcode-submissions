class Solution:

    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
            Given 2d array of heights (elevations)
            Pacific Ocean borders our top and our left sides
            Atlantic Ocean borders the bottom and right sides
            Water can Flow up down left right, to neighboring cells with height equal or lower

            Goal: Find all cells where water can flow from that cell to both the Pacific and Atlantic Oceans
            I think it is likely easier to think about this in reverse
            Find all cells that can be reached starting from the ocean assuming we can only go to cells >=

            Alright so so far I am thinking we do some kind of multisource bfs with no visited array so that it can be
            visited again by the Atlantic cells, should still be fine as far as cycles cuz it can never go lower
            Could also maintain 2 visited arrays which would likely be faster
            Yeah lets do that have a cell for visited by pacific and visited by atlantic and if we have been visited from our
            pacific we wouldnt visit from pacific again unless that parent is also atlantic. 

        """
        dx = [1, 0, -1, 0]
        dy = [0,1,0,-1]
        def bfs(q, visited):
            while q:
                curr = q.popleft()
                row = curr[0]
                col = curr[1]


                for i in range(4):
                    new_row = row + dx[i]
                    new_col = col + dy[i]

                    if new_row < ROW and new_col < COL and new_row >= 0 and new_col >= 0:
                        if heights[new_row][new_col] >= heights[row][col]:
                            if (new_row, new_col) not in visited:
                                visited.add((new_row, new_col))
                                q.append([new_row, new_col])
                    
        ROW = len(heights) 
        COL = len(heights[0])
        q = deque()

        pacific_visited = set()

        # add the pacific ones
        for col in range(0, COL):
            q.append([0, col])
            pacific_visited.add((0,col))
        
        for row in range(0, ROW):
            q.append([row, 0])
            pacific_visited.add((row,0))

        print("pacific", pacific_visited)


        bfs(q, pacific_visited)
        print("pacific", pacific_visited)

        
        atlantic_visited = set()
        # add the atlantic ones
        for col in range(0, COL):
            q.append([ROW-1, col])
            atlantic_visited.add((ROW-1, col))
        
        for row in range(0, ROW):
            q.append([row, COL-1])
            atlantic_visited.add((row, COL-1))


        bfs(q, atlantic_visited)

        result = [] # could remove to save space and spend a bit more time
        print("pacific", pacific_visited)
        print("atlantic", atlantic_visited)

        for cell in pacific_visited:
            print(cell)
            if cell in atlantic_visited:
                result.append(cell)

        return result









