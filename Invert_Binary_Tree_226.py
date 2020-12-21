# Invert a binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Base Case
        if not root:
            return None
        else:
            # swap the left and the right (swaps 2, 7)
            root.left, root.right = root.right, root.left
            # write recursive to swap the children  (1, 3, 6, 9)
            # call self.invertTree (recursive solution)
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

# https://www.youtube.com/watch?v=us16ghTzrZg