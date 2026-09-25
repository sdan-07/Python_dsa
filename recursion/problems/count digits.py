def count_digits(num):
    def helper(count, num):
        if num == 0: return count

        return helper(count+1, num // 10)
    return helper(0, num)


if __name__ == '__main__':
    num=64792
    print(count_digits(num))