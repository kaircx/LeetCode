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
            before=tmp#3
            after=tmp.next#
            if after!=None:
                tmp=after.next#None
            else:
                return begin
            before.next=after.next#None
            after.next=before#3
            if archive is not None:
                archive.next=after
            if tmp!=None:
                archive=before
                pass  
            else:
                break          
        return begin
            
            
        