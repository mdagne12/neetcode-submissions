# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(curr, upper_bound, lower_bound):
            if curr is None:
                return True

            if lower_bound < curr.val < upper_bound:
                left_bool = helper(curr.left, min(upper_bound, curr.val), lower_bound)
                right_bool = helper(curr.right, upper_bound, max(lower_bound, curr.val))
                return left_bool and right_bool
            else:
                return False

        return helper(root, float("inf"), float("-inf"))