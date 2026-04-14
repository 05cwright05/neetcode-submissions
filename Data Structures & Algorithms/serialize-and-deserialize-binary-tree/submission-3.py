# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # we need to know where nulls are we will denote those with a +,
        # it is likely best to do a lelve traversal
        # so if the tree was a linked list to the right (5,7,9) we would have to store as 
        # [5+7+9]
        q = deque()
        q.append(root)
        output_str = []
        while q:
            curr = q.popleft()
            if not curr:
                output_str.append(",+")
            else:
                output_str.append(f",{curr.val}")
                q.append(curr.left)
                q.append(curr.right)
        output = "".join(output_str)
        if output[0] == ",":
            return output[1:]


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if data[0] == "+":
            return None
        

        # can do a bfs through the serialized string

        q = deque()
        root = TreeNode(vals[0])
        q.append(root)

        index = 1
        while q:
            curr = q.popleft()
            if index >= len(vals):
                return root
            if vals[index] != "+":
                left_child = TreeNode(vals[index])
                curr.left = left_child
                q.append(left_child)
            index+=1
            if index >= len(vals):
                return root
            if vals[index] != "+":
                right_child = TreeNode(vals[index])
                curr.right = right_child
                q.append(right_child)
            index+=1

        return root

            

