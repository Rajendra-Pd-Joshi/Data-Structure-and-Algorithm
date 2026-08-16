# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr is not None:
            curr = curr.next
            length += 1
        
        curr = head
        for _ in range(0,length//2):
            curr = curr.next
        return curr