def fibo(n):
    if n<=1: return n

    last = fibo(n-1)    # first rec call execute- last
    slast = fibo(n-2)   # second rec call execute- slast
    return last + slast

#     return fibo(n-1) + fibo(n-2)

if __name__ == '__main__':
    print(fibo(4))