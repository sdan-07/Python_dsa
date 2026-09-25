def check_palindrome(s):
    if len(s) < 2: return True

    def helper(l,r,s):
        if l>=r: return True

        if s[l] != s[r]: return False

        return helper(l+1, r-1, s)
    return helper(0, len(s)-1, s)



if __name__ == '__main__':
    s = "madam"
    print(check_palindrome(s))