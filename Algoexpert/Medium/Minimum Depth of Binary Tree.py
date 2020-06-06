# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        def helper(root):
            if not root: return 0
            if root.left and root.right:
                return(1+ min(helper(root.left), helper(root.right)))
            elif root.left:
                return(1+ helper(root.left))
            else:
                return(1+ helper(root.right))
        return helper(root)