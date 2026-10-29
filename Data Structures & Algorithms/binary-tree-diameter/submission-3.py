# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # stack = [(root, False)]
        # max_height_dict = {}
        # diameter = 0

        # while stack:
        #     node, visited = stack.pop()

        #     if not visited:
        #         stack.append((node, True))
        #         if node.left:
        #             stack.append((node.left, False))
        #         if node.right:
        #             stack.append((node.right, False))
            
        #     else:
        #         if not node.left:
        #             left_height = 0
        #         else:
        #             left_height = max_height_dict.pop(node.left)

        #         if not node.right:
        #             right_height = 0
        #         else:
        #             right_height = max_height_dict.pop(node.right)
            
        #         diameter = max(diameter, left_height + right_height)
        #         max_height_dict[node] = max(left_height, right_height) + 1
        
        # return diameter
        self.diameter = 0

        def depth(node):
            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            self.diameter = max(self.diameter, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.diameter

