class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        sum = 0
        for ch in operations:
            if ch != "+" and ch != "D" and ch != "C":
                stack.append(int(ch))
            elif ch == "+":
                stack.append(stack[-1] + stack[-2])
            elif ch == "C":
                stack.pop()
            elif ch == "D":
                stack.append(stack[-1] * 2)

        for item in stack:
            sum += int(item)

        return sum
