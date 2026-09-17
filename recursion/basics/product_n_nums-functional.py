def product(n):
    if n==1: return n

    return n * product(n-1)

if __name__ == '__main__':
    print(product(5))