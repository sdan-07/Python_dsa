def merge_sort(nums):
    n=len(nums)
    if n<=1: return nums
    mid = n // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)

def merge(left,right):
    res=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

if __name__ == '__main__':
    for num in merge_sort([3,1,7,2,8,9]):
        print(num, end=" ")