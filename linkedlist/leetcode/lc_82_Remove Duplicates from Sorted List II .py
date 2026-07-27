# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur:
            isDup = False

            while cur.next and cur.val == cur.next.val:
                isDup = True
                cur = cur.next

            if isDup:
                prev.next = cur.next
            else:
                prev = prev.next

            cur = cur.next

        return dummy.next
