# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def isBST(root, low, high):
            if not root: return True
            val = root.val
            if low < val < high:
                return(isBST(root.left, low, val) and isBST(root.right, val, high))
            else:
                return False

        return isBST(root, float("-inf"), float("inf"))