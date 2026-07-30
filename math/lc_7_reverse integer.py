class Solution:
    def reverse(self, x: int) -> int:
        num = 0

        if x < 0:
            x = x * -1
            num = int(str(x)[::-1]) * -1

        else:
            num = int(str(x)[::-1])

        if num < -2 ** 31 or num > 2 ** 31 - 1: return 0

        return num
