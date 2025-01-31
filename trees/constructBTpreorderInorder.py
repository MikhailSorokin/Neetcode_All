# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # INEFFICIENT O(n^2) time
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        split = inorder.index(root.val)

        left_of_root = inorder[0:split]
        right_of_root = inorder[split + 1:]

        if left_of_root:
            root.left = self.buildTree(preorder[1:split + 1], left_of_root)

        if right_of_root:
            root.right = self.buildTree(preorder[split + 1:], right_of_root)

        return root
        
    # EFFICIENT O(n) time, no "index" method. Use hashmap to remember inorder indices
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}
        
        self.pre_idx = 0
        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)

# preorder -> root first
# inorder -> root center