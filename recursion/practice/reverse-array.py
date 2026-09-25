def reverse_array(nums):
    def helper(l,r,nums):
        if l>=r: return nums

        nums[l], nums[r] = nums[r], nums[l]

        return helper(l+1, r-1, nums)
    return helper(0, len(nums)-1, nums)


if __name__ == '__main__':
    nums=[1,2,3,4,5,6]
    for num in reverse_array(nums):
        print(num, end=" ")