# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        ptr = head
        while ptr:
            nums.append(ptr.val)
            ptr = ptr.next

        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            if nums[l] == nums[r]:
                l += 1
                r -= 1
            else:
                return False
        return True