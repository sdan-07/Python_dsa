# Palindrome number
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    rev = 0
    num = x
    while num != 0:
        rev = rev * 10 + num % 10
        num = num // 10

    if rev == x:
        return True
    return False

result = isPalindrome(121)
print(result)

