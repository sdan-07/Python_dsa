#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    # Write your code here
    codeArr = list(code)
    letters = []
    for c in codeArr:
        if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
            letters.append(c)

    i = 0
    j = len(letters) - 1
    while i < j:
        if letters[i] == letters[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
