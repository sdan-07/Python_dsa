def fact(n):
    # product of numbers
    if n==1: return n

    return n * fact(n-1)


if __name__ == '__main__':
    r = fact(6)
    print(r)