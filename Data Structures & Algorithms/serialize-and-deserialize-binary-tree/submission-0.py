# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                nodesPreorder.append("null")
                return

            nodesPreorder.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        nodesPreorder = []
        dfs(root)
        string = ','.join(nodesPreorder)
        return string
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def dfs():
            val = next(vals)
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        vals = iter(data.split(','))
        return dfs()



