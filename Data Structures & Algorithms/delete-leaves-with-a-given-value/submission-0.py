# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """

        given:
            - root of binary tree
            - integer target
        
        Goal:
            - Delete all leaf nodes where val = target

        Note: if we delete a node and a node becomes a leaf node we now need to delete it as appropriate

        Thus we need a bottom up approach
        Strat
        We will recurse all the way to bottom using a postorder traversal,

        as the check step we will see if we have no children (right and left are None)
        and our value is equal to target we will pass up true if deleted so parent knows to set that side to None or not
        """

        def dfs(curr):
            if not curr:
                return

            dfs(curr.left)
            dfs(curr.right)
            print("visiting", curr.val)
            if curr.left and curr.left.val < 0:
                curr.left = None
            if curr.right and curr.right.val < 0:
                curr.right = None
            # if we are a leaf node then if our value is the target
            # mark us for deletion by parent
            if not curr.left and not curr.right:
                if curr.val == target:
                    curr.val *= -1 # so our parent can check
        dfs(root)
        if root.val < 0:
            return None
        return root
         