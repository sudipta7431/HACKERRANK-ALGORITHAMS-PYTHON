#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Write your code here
    n = len(arr)
    sum_all = 0
    for i in range(n):
        sum_all += arr[i]
    sum_all_min = sum_all - max(arr)
    sum_all_max = sum_all - min(arr)
    
    print(f'{sum_all_min} {sum_all_max}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
