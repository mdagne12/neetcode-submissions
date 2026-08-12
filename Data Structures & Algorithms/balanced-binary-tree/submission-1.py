# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if curr is None:
                return (0, True)

            left_count, left_bool = dfs(curr.left)
            right_count, right_bool = dfs(curr.right)

            curr_count = 1 + max(left_count, right_count)
            curr_bool = left_bool and right_bool and -1 <= left_count - right_count <= 1
            return curr_count, curr_bool

        _, result = dfs(root)
        return result