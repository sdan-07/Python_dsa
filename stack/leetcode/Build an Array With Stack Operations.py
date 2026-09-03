class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        res = []
        for i in range(1, n + 1):
            stack.append(i)
            res.append("Push")

            if stack[-1] != target[len(stack) - 1]:
                stack.pop()
                res.append("Pop")

            if stack == target: break

        return res
