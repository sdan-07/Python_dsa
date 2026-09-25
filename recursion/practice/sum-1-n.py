def sum_oneToN(n):
    if n==0: return n

    return n + sum_oneToN(n-1)

if __name__ == '__main__':
    print(sum_oneToN(5))
