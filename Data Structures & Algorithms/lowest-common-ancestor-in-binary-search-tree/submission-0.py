# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lower_bound = float("-inf")
        upper_bound = float("inf")
        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                upper_bound = min(upper_bound, curr.val)
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                lower_bound = max(lower_bound, curr.val)
                curr = curr.right
            else:
                return curr
