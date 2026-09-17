# def calc_sum(n, sum):
#     if n < 1:
#         print(sum)
#         return
#
#     calc_sum(n-1, sum+n)
def calc_sum(n):
    def helper(n, sum):
        if n < 1:
            print(sum)
            return
        helper(n-1, sum + n)
    helper(n, 0)

if __name__ == '__main__':
    calc_sum(4)