# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # This approach would be in V+E = 2V, we would need to also run a bfs which is 2v
        # there may be a way to do it  one pass tho if you want me to keep thinking

        # so for this we would need a recursive something like this 
        lowest_common_ancestor = None
        def recurse(curr):
            nonlocal lowest_common_ancestor
            if curr is None: 
                return [False, False]

            
            bool_have_p = False
            bool_have_q = False
            
            bool_values = recurse(curr.left)
            bool_values2 = recurse(curr.right)
            bool_have_p = bool_values[0] or bool_values2[0] or curr.val == p.val
            bool_have_q = bool_values[1] or bool_values2[1] or curr.val == q.val



            if bool_have_p and bool_have_q:
                if lowest_common_ancestor is None:
                    lowest_common_ancestor = curr

            return [bool_have_p, bool_have_q]

        recurse(root)
        return lowest_common_ancestor
