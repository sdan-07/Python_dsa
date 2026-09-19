def reverse(nums):
    def rev(l,r,nums):
        if l>=r: return nums

        nums[l], nums[r] = nums[r], nums[l]

        return rev(l+1, r-1, nums)

    return rev(0, len(nums)-1, nums)


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    for num in reverse(nums):
        print(num, end=" ")