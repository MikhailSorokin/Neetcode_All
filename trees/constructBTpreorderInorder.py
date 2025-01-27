# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        temp = inorder.index(root.val)

        left_of_root = inorder[0:temp]
        right_of_root = inorder[temp + 1:]

        if left_of_root:
            root.left = self.buildTree(preorder[1:temp + 1], left_of_root)

        if right_of_root:
            root.right = self.buildTree(preorder[temp + 1:], right_of_root)

        return root

# preorder -> root first
# inorder -> root center