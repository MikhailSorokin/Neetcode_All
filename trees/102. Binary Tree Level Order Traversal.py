# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])
        level = 0
        while q:
            tmp = []
            for _ in range(0,len(q)):
                cur = q.popleft()
                if cur.left is not None:
                    q.append(cur.left) 
                if cur.right is not None:
                    q.append(cur.right)
                tmp.append(cur.val)
            res.append(tmp)
            
            #print(f'Level: {level}, curr: {tmp}')
            level += 1
        return res
