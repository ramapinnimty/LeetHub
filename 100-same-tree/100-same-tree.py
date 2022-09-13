# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Approach: Recursive; Time: O(n); Space: O(n)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Edge case: If both `p` & `q` are null
        if not p and not q:
            return True

        # Check if:
        #   - both `p` & `q` are not `None`
        #   - the values at both `p` & `q` are equal
        #   - recursively verify this for both left- and right- subtrees
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False