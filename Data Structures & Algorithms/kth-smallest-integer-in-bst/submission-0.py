# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #first thought is that we go thru the tree and for every node we see
        # we add it to a min-heap this approach would be NlogN + k 

        # wondering if we can do in a single pass give =n that it is indeed a binary serach tree,
        # surely there is a way to exploit this
        # definitely gotta be a way.
        # like we recurse down using a postorder traversal and then we recurse back up the stack n-1 times 
        # like if i visit all nodes ysing an in order traversal and then add them as a list as i do that then the k-1 element will be what im looking for
        nodes = []
        def dfs(curr):
            if curr == None:
                return 
            dfs(curr.left)
            nodes.append(curr.val)
            dfs(curr.right)
        dfs(root)
        if k - 1 < len(nodes):
            return nodes[k-1]
        else:
            return -1



