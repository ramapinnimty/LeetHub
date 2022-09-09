# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Approach: Recursion; Time: O(H); Space: O(H)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # By comparing `p` and `q`, we'll get 4 cases

        # Case-1: If `p` and `q` are on either side i.e, they split
        # `p` is on left side & `q` is on right side or vice-versa
        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
            return root

        # Case-2: If `p` and `q` are on the left side
        # check only the left subtree
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Case-3: If `p` and `q` are on the right side
        # check only the right subtree
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Case-4: If either `p` or `q` is the ancestor node
        elif p.val == root.val or q.val == root.val:
            return root