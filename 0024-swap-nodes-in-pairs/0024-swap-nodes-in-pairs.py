# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        begin = head.next
        tmp = head
        archive=None
        while True:
            before=tmp
            after=tmp.next
            if after!=None:
                tmp=after.next
            else:
                break
            before.next=after.next
            after.next=before
            if archive is not None:
                archive.next=after
            if tmp!=None:
                archive=before
            else:
                break          
        return begin
            
            
        