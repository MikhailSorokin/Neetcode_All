# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        newLst = []
        queue = deque([root])

        while queue:
            lastElem = 0
            n = len(queue)
            # Level-order traversal first
            for i in range(n):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == n - 1:
                    newLst.append(node.val)


        print(newLst)
        return newLst

            