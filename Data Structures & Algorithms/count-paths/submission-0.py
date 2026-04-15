class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # given an mxn grid where you can move down or right at any point in time
        # ONLY DOWN and RIGHT
        # goal is to return the number of possible unique paths that can be taken from top left corner to bottom right corner
        # i think for each square it is likely the number of ways to get to the square above it plus the number
        # of ways to get to the cell to the left of it

        # from experimentation this seems correct so lets code it up 

        dp = [[0]*n for _ in range(m)]

        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue
                row_above = row -1
                value_above = 0
                if row_above >= 0:
                    value_above = dp[row_above][col]

                col_left = col - 1
                value_left = 0
                if col_left >= 0:
                    value_left = dp[row][col_left]

                dp[row][col] = value_above + value_left
        print(dp)
        return dp[-1][-1]