# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        All values are unique so we do not need to worrry about that 

        Basically just traverse starting from the root

        if target < curr.val
        curr = curr.left
        if target > curr.val
        curr = curr.right
        if curr is null then we know we should insert there (so the previous)

        """

        prev = root
        curr = root
        if root is None:
            root = TreeNode(val)
            return root

        while curr:
            if val < curr.val:
                prev = curr
                curr = curr.left
            elif val > curr.val:
                prev = curr
                curr = curr.right

        new_node = TreeNode(val)
        if val < prev.val:
            prev.left = new_node
        else:
            prev.right = new_node
        return root

        
