# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):
            nonlocal k

            if node is None:
                return None

            left = dfs(node.left)
            k -= 1
            if k == 0:
                return node
            right = dfs(node.right)
            return left or right

        res = dfs(root)
        return res.val if res else 0