# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # https://leetcode.com/problems/reverse-linked-list-ii/
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left >= right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = None
        curr = dummy.next
        lastHead = dummy
        lastTail = None
        
        i = 0
        left -= 1
        right -= 1
        while curr != None and left <= right:
            if i < left:
                lastHead = curr
                curr = curr.next
                i += 1
            else:
                if not lastTail:
                    lastTail = curr
                # Below logic for reversing whole list in sublist
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                left += 1
                i += 1

        if lastHead:
            lastHead.next = prev
        if lastTail:
            lastTail.next = curr

        return dummy.next