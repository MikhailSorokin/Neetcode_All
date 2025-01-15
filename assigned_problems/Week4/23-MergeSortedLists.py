# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def merge(self, list1, list2):
        curr = dummy = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1, curr = list1.next, list1
            else:
                curr.next = list2
                list2, curr = list2.next, list2

        if list1 or list2:
            curr.next = list1 if list1 else list2
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
    
        while len(lists) > 1:
            l1 = lists.pop()
            l2 = lists.pop()
            lists.append(self.merge(l1, l2))

        return lists[0]