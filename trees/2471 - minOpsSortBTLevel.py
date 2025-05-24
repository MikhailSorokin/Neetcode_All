# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, Counter 

# Problem 2471 - https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/
class Solution:
    def listMinSwaps(self, lst: [int]) -> int:
        # Get minimum value every iteration step
        # See if we have to swap
        n = len(lst)
        swaps = 0
        copyLst = sorted(lst)

        posMap = {val : idx for idx, val in enumerate(lst)}

        for i in range(len(lst)):
            if lst[i] != copyLst[i]:
                curPos = posMap[copyLst[i]]
                posMap[lst[i]] = curPos
                lst[curPos] = lst[i] 

                swaps += 1

        return swaps


    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = []
        queue = deque([root])
        level = 0
        minSwaps = 0

        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1    
            if level != 1:
                minSwaps += self.listMinSwaps(temp)

        return minSwaps


            
