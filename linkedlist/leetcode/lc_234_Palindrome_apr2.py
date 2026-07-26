# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast: slow = slow.next

        fast = head
        slow = self.reverseList(slow)

        # check palindrome
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True

    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nextPtr = curr.next
            curr.next = prev
            prev = curr
            curr = nextPtr
        return prev



