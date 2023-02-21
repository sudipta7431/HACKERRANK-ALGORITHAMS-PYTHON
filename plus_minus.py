#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    posative = 0
    negative = 0
    newtral = 0
    for i in arr:
        if i > 0:
            posative += 1
        elif i < 0:
            negative += 1
        else:
            newtral +=1
    print("%.6f" % (posative/len(arr)))
    print("%.6f" % (negative/len(arr)))
    print("%.6f" % (newtral/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

