#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    # Write your code here
    sum1_l_r = 0
    sum1_r_l = 0
    n = len(arr)
    for i in range(n):
        sum1_l_r += arr[i][i]
        i +=1
    
    for j in range(n):
        sum1_r_l += arr[j][n-j-1]
        j +=1
    
    return abs(sum1_l_r-sum1_r_l)
        
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
