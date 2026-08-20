# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(a_tree, b_tree):
            if a_tree is None and b_tree is None:
                return True
            elif a_tree and b_tree and a_tree.val == b_tree.val:
                left = isSameTree(a_tree.left, b_tree.left)
                right = isSameTree(a_tree.right, b_tree.right)
                return left and right
            else:
                return False

        if isSameTree(root, subRoot):
            return True
        elif root is None:
            return False
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        