#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

def findSmallestMissingPositive(orderNumbers):
    n = len(orderNumbers)
    if n <= 1: return n + 1

    minimum = float('inf')
    check = []
    for i in range(1, n + 1):
        check.append(i)

    for num in check:
        if num not in orderNumbers:
            minimum = min(minimum, num)

    return minimum


if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
