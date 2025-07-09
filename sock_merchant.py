#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    
    color_count = {}
    
    # Count how many socks of each color
    for color in ar:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    # Count pairs
    pairs = 0
    for count in color_count.values():
        pairs += count // 2  # Divide by 2 to get number of pairs

    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
