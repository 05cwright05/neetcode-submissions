# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #since we know that the number of nodes in the tree is 1000 that means there are a max of 1000 sublists
        # could try to optimize this stupid instantiation of 1000 empty lists, but essntially, the idea will be to use breadth first serch
        # the head we will makr as level 0 and whenever we traverse to children we up the level.
        # then we add to the respective list when it is popped out of the list.
        # probably smarter to basically see if the number it has is >= len(list_of_list) if so create a new [] and add us too it
        # other wise add as usual
        if not root:
            return []
        q = deque()
        q.append([root, 0])
        result = []
        while q:
            curr = q.popleft()
            node = curr[0]
            level = curr[1]
            if level >= len(result):
                result.append([node.val])
            else:
                result[level].append(node.val)

            if node.left:
                q.append([node.left, level + 1])
            if node.right:
                q.append([node.right, level+1])
        return result
