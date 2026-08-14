# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p_tree, q_tree):
            if not p_tree and not q_tree:
                return True

            if not p_tree or not q_tree:
                return False

            if p_tree.val != q_tree.val:
                return False

            left_bool = dfs(p_tree.left, q_tree.left)
            right_bool = dfs(p_tree.right, q_tree.right)

            return left_bool and right_bool

        return dfs(p, q)
        

            
        