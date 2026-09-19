def isPalindrome(s):
    def check(l,r,s):
        if l>=r: return True

        if s[l] != s[r]: return False

        return check(l+1, r-1, s)

    return check(0, len(s)-1, s)


if __name__ == '__main__':
    s = "madam"
    print(isPalindrome(s))