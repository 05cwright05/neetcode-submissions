# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    best_path = 0
    def recHeightFinder(self, curr):
        if curr is None:
            return 0
        left_height = self.recHeightFinder(curr.left)
        right_height = self.recHeightFinder(curr.right)

        self.best_path = max(self.best_path, left_height+right_height+1)
        return max(left_height + 1, right_height + 1)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # the longest path will occur by maximizing the following
        # path is defined as depth of left subtree + right subtree
        # so step one is to find that height recursively 

       self.recHeightFinder(root)
       return self.best_path -1 