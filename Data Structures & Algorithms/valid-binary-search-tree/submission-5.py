# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # my first idea is to traverse the tree in order and remember
        # then traverse the list and ensure each node is less than the next
        # this is O(N + N) or 2N or O(N)

        # can maybe do in single pass but im most comfortable with this approach
        inorder = []
        def dfs(curr):
            if curr is None:
                return
            dfs(curr.left)
            inorder.append(curr.val)
            dfs(curr.right)
        dfs(root)
        for i in range(1, len(inorder)):
            if inorder[i-1] >= inorder[i]:
                return False
        return True