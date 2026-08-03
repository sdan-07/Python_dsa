# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l=0
        r = len(nums)-1

        return self.buildTree(l,r,nums)

    def buildTree(self,l,r,nums):
        if l > r: return None
        mid = (l+r) // 2

        node = TreeNode(nums[mid])
        node.left = self.buildTree(l, mid-1, nums)
        node.right = self.buildTree(mid+1, r, nums)

        return node
