from collections import Counter

def intersect(nums1, nums2):
    res = []
    counts = Counter(nums1)

    for num2 in nums2:
        if counts[num2] > 0:
            res.append(num2)
            counts[num2] -= 1

    return res

nums1, nums2 = [1,2,2,3], [2,3,4]
print(intersect(nums1, nums2))
