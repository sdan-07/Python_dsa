# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nums = []
        ptr=head
        while ptr:
            nums.append(ptr.val)
            ptr=ptr.next

        nums.pop(-n)

        dummy=ListNode()
        cur = dummy

        for num in nums:
            cur.next = ListNode(num)
            cur=cur.next
        return dummy.next