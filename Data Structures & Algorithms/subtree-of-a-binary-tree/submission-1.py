# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True

            if root and subRoot:
                if root.val == subRoot.val:
                    return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
                else:
                    return False

            return False

        if not root:
            return False

        queue = deque([root])
        while queue:
            root = queue.popleft()
            if root and root.val == subRoot.val:
                if isSameTree(root, subRoot):
                    return True

            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

        return False


        
