# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 86 - Partition list
# https://leetcode.com/problems/partition-list/
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        headLT = ListNode()
        currLT = headLT
        headGTE = ListNode()
        currGTE = headGTE

        curr = head

        while curr != None:
            if curr.val < x:
                currLT.next = curr
                currLT = curr
            else:
                currGTE.next = curr
                currGTE = curr

            curr = curr.next

        currGTE.next = None
        currLT.next = headGTE.next

        return headLT.next