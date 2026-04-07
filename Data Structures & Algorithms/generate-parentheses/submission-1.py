class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Alright so if we dont have an open parenthesis we CANNOT put a clsoe parentehseis
        # Otherwise we have either as a choice
        # So we should maintain a count: num_open
        # If there is 1 open and 1 clsoe that should be said to be 0
        string = []
        output = []
        def backtrack(string, num_open, open_left, close_left):
            if open_left == 0 and close_left == 0:
                output.append("".join(string))
                return
            if open_left > 0:
                string.append("(")
                backtrack(string, num_open+1, open_left-1, close_left)

                string.pop()
            if num_open > 0:
                num_open-=1
                close_left-=1
                string.append(")")
                backtrack(string, num_open, open_left, close_left)
                string.pop()

        backtrack([], 0, n, n)

        return output