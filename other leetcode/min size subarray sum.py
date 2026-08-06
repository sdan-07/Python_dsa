class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        i=0
        j = 0
        min_size = float('inf')

        while j<len(nums):
            sum += nums[j]

            while sum >= target:
                min_size = min(min_size, j-i+1)
                sum -= nums[i]
                i+=1
            j+=1

        if min_size == float('inf'):
            return 0
        return min_size