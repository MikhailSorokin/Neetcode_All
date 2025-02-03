# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       
        if root == None:
            return True
 
        def height(node):
            if node == None:
                return 0

            return 1 + max(height(node.left), height(node.right))

        if abs(height(root.left) - height(root.right)) > 1:
            return False
            
        return self.isBalanced(root.left) and self.isBalanced(root.right)