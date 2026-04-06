# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    isBalanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def recHeightFinder(curr):
            nonlocal isBalanced
            if not curr:
                return 0
            left = recHeightFinder(curr.left)
            right = recHeightFinder(curr.right)
            if abs(left-right) > 1:
                isBalanced = False
            return max(left + 1, right+1)

        recHeightFinder(root)

        return isBalanced