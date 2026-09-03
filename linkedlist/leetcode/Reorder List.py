# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        stack = []
        ptr = head
        while ptr:
            stack.append(ptr)
            ptr = ptr.next

        ptr = head
        while ptr:
            node = stack.pop()

            if ptr == node or ptr.next == node:
                node.next = None
                break

            nxt = ptr.next
            ptr.next = node
            node.next = nxt
            ptr = nxt