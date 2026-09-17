class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        numset = set(nums1)
        res = []
        for num in nums2:
            if num in numset:
                res.append(num)
                numset.remove(num)

        return res