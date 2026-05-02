class Solution:



    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Given a 2d grid of characters board

        Given a string word

        Return true if the word is present in the grid

        False if not

        For it to be present it must be possible to form it with a path in the board horizontally or vertically neighboing cells

        My first thought it to starts a bfs from any cell that is the letter that starts this word

        In the worst case though i think this could end up being N^4 unless i am missing somehting, yeah i think thats possible

        If we do a multi source bfs the problem is that i have to be allowed to reuse the starting letter

        I am leaning toward this brute force bfs but dont like it

        Sounds like the bfs is lowkenuinely fast enoygh tho so ima just hit that

        The board is tiny 

        Ok but this is cooked cuz it matters with path we take while bfs doesnt give a shit
        """

        ROW = len(board)
        COL = len(board[0])

        dr = [1,0,-1,0]
        dc = [0,1,0,-1]

        def dfs(row,col,index):
            if index == len(word) - 1:
                return True
            for i in range(4):
                new_row = row + dr[i]
                new_col = col + dc[i]
                if new_row >= 0 and new_col >= 0 and new_row < ROW and new_col < COL:
                    # This line handles visited cuz obs # cannot be our next letter
                    if board[new_row][new_col] == word[index+1]:
                        tmp = board[new_row][new_col]
                        board[new_row][new_col] = "#" #visited

                        if dfs(new_row, new_col, index + 1):
                            return True
                        board[new_row][new_col] = tmp
            return False


        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == word[0]:
                    # run a dfs
                    tmp = board[row][col]
                    board[row][col] = "#"
                    if dfs(row, col, 0):
                        return True
                    print(board)
                    board[row][col] = tmp
        return False
                   


                        









