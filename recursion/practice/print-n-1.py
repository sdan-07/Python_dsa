def show_nToOne(n):
    if n==0: return

    print(n, end=" ")
    show_nToOne(n-1)

if __name__ == '__main__':
    show_nToOne(8)