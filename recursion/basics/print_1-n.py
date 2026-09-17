def print_num(n):
    if n < 1: return

    print_num(n-1)
    print(n, end=" ")

if __name__ == '__main__':
    print_num(7)