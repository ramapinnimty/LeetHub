# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time: O(n); Space: O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: Check if we have 0 nodes
        if root is None:
            return 0

        # Base case: Check if we have 1 node or if we are at the leaf node
        if root.left is None and root.right is None:
            return 1

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))