def print_num_reversed(n):
    if n < 1: return

    print(n, end=" ")
    print_num_reversed(n-1)


if __name__ == '__main__':
    print_num_reversed(7)