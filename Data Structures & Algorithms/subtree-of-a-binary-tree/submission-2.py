# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # strategy
        # search root until we find the subroot
        # if no find it then we know it is not the same
        # otherwise start a traversal step from there and ensure they match
        # question: can there be duplicate values? cuz if so we may need to do this mutiple times
        # lets start by assuming no
        def verifyTree(curr, subCurr):
            if curr is None and subCurr is None:
                return True
            if curr is None:
                return False
            if subCurr is None:
                return False
            if curr.val != subCurr.val:
                return False
            return verifyTree(curr.left, subCurr.left) and verifyTree(curr.right, subCurr.right)

        def searchForSubRoot(curr, subRoot):
            if not curr:
                return False
            
            if curr.val == subRoot.val:
                #conduct a search here and make sure they match everystep
                do_they_match = verifyTree(curr, subRoot)
                if do_they_match:
                    return do_they_match
            
            return searchForSubRoot(curr.left, subRoot) or searchForSubRoot(curr.right, subRoot)
                
            
        
        return searchForSubRoot(root, subRoot)
