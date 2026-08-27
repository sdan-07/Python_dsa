class Solution:
    def findLHS(self, nums: List[int]) -> int:
        maxlen = 0
        freq=Counter(nums)


        for num in freq:
            if num < 0 and num + 1 in freq:
                maxlen = max(maxlen, freq[num] + freq[num+1])
            elif num > 0 and num-1 in freq:
                maxlen = max(maxlen, freq[num] + freq[num-1])


        return maxlen