def calc_sum(n):
    if n == 0: return 0

    return n + calc_sum(n-1)

if __name__ == '__main__':
    print(calc_sum(7))