class Solution:
    def leaders(self, arr):
        # code here
        res = []
        n = len(arr)
        largest = arr[-1]
        res.append(largest)

        for i in range(n - 2, -1, -1):
            if largest <= arr[i]:
                res.append(arr[i])
                largest = arr[i]

        res.reverse()
        return res