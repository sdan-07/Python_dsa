class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        longest = 1
        myset = set(nums)

        for num in myset:
            if num - 1 not in myset:
                # inc same length
                inc = 1
                while num + inc in myset:
                    inc += 1
                longest = max(longest, inc)

        return longest