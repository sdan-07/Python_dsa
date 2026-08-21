def solve(nums):
    size = len(nums)
    mid = 1
    sum = i = 0
    j = mid + 1
    # maxRes = float('-inf')

    while i <= mid:
        sum += nums[i]
        i += 1

    maxRes = max(nums[mid + 1:])

    return maxRes * sum


# nums = [5,4,3,2,1]
nums = [10, 20, 30]
print(solve(nums))

