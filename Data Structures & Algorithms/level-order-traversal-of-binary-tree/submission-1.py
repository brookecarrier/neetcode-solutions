# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        output = []

        if not root:
            return output

        q = deque()
        q.append(root)

        while q:
            levelNodes = []
            levelSize = len(q)
            for i in range(levelSize):
                node = q.popleft()
                levelNodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            output.append(levelNodes)
        
        return output