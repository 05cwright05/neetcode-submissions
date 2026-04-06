# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # i am thinking some kind of bfs where we remeber the biggest along the path as we spread
        # increment count of node when we visit a node taht is bigger than the biggest on the path it came from

        q = deque()
        #q.popleft()
        #q.append()
        q.append([root, root.val])
        num_good = 0
        while q:
            curr, biggest_on_path = q.popleft()
            value = curr.val
            if value >= biggest_on_path:
                num_good+=1

            if curr.left:
                q.append([curr.left, max(biggest_on_path, value)])
            if curr.right:
                q.append([curr.right, max(biggest_on_path, value)])
        return num_good



