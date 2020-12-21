# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# 1 + max(1 + max(l, r), right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 1 + maximum(left, right)
        # Call function on left subtree, as well as right subtree
        # When value returns => we'll take the maximum of both sides 
        # Height of three is one plus the maximum of rigght or left subtree
        # Base case => if root is empty => return zero
        if root is None:
            return 0
        else:
            return 1 + max(
                # Helper function. Returns height of left and right tree
                # Then take the maximum 
                # Once we have the maximum, just add one to it.     
                self.maxDepth(root.left),
                self.maxDepth(root.right)
            )