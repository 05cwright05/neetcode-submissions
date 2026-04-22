# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """

        Given a binary tree  return only the nodes that are visible from the right

        hmm, how do we approach this:

        First option:
            - We can do a bfs through the whole tree
            - and have a list of level -> nodes in that level, probbaly hashmap cuz we dont know height of tree
            - but for optimization we are going to ensure we visit left or right so instead of a hashmap to  alist
                it can be a hashmap to a signle value which is the most recently added
                the most recently added at a given level will always be right most

        This would be an O(n) pass using bfs, finding level in hashmap is O(1) for a total of O(n) at the asymptote i dont think we can any better
        Do you want me to implmenet this or try to come up with a stronger solution
        """

        q = deque()
        if not root:
            return []

        levels = {}
        q.append([root, 0]) # starting node, starting level

        while q:
            curr = q.popleft()
            node = curr[0]
            level = curr[1]
            levels[level] = node.val
            if node.left:
                q.append([node.left, level+1])
            if node.right:
                q.append([node.right, level+1])

        return list(levels.values())