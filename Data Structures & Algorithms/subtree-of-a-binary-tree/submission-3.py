# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # my strat was highkey goated
        # but apparently we can serialize each tree and then see if subRoot is a substring in the main string
        # python does with .contains i think

        # we can traverse each tree as a breadth first search and see if the substring is there
        s1 = ""
        s2 = ""
        def dfs(root,curr_str) -> str:
            q = []
            q.append(root)
            while len(q) > 0:
                curr = q.pop()
                if curr:
                    curr_str+=str(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
                else:
                    curr_str+="#"
            return curr_str
        s1 = dfs(root, "")
        s2 = dfs(subRoot, "")

        print(s1, s2)
        if s2 in s1:
            return True
        return False


