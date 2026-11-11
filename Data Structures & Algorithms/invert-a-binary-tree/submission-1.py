# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # stack = [root]

        # while stack:
        #     current = stack.pop()
            
        #     if current:
        #         current.left, current.right = current.right, current.left
        #         stack.extend([current.left, current.right])
        
        # return root

        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root