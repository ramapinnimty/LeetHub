# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time: O(n); Space: O(h) ~ O(n) stack space
class Solution:
    def isLeaf(self, root):
        return root.left is None and root.right is None

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: Check if we have 0 / 1 node or if we are at the leaf node
        if root is None or self.isLeaf(root):
            return root

        # Invert the sub-trees
        inverted_left  = self.invertTree(root.left)
        inverted_right = self.invertTree(root.right)

        # Swap
        root.left  = inverted_right
        root.right = inverted_left

        return root