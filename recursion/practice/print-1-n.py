def show_oneToN(n):
    if n==0: return

    show_oneToN(n-1)
    print(n, end=" ")

if __name__ == '__main__':
    show_oneToN(5)