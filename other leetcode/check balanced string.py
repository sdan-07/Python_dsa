class Solution:
    def isBalanced(self, num: str) -> bool:
        number = [int(x) for x in num]
        number.append(0)
        oddsum = evensum = 0
        i = 0
        j = 1
        while j < len(number):
            evensum += number[i]
            oddsum += number[j]
            i += 2
            j += 2

        if evensum == oddsum:
            return True
        return False

