class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)
        nums1.sort()

        i=0
        j=len(nums1)-1
        while i<=j:
            if i==j:
                return float(nums1[i])
            i+=1
            j-=1

        return (nums1[i]+nums1[j])/2

