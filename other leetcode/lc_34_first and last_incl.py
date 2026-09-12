# This solution is not O(log n) which leetcode expects
# This solution is of O(n^2)

class Solution:
    def __init__(self):
        pass

    def searchRange(self, nums, target):
        n = len(nums)
        res = []
        i = 0
        while i < n:
            if nums[i] == target:
                res.append(i)

                while nums[i] == target:
                    i += 1
                res.append(i-1)
            else:
                i += 1

        if not res: return [-1, -1]
        return res

def main():
    sol = Solution()
    nums=[1,2,2,2,2,4,5]
    print(sol.searchRange(nums, 2))

main()