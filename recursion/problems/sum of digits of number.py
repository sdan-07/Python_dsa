def sum_of_digits(num):
    if num == 0: return num

    return sum_of_digits(num//10) + num%10


if __name__ == '__main__':
    print(sum_of_digits(32))