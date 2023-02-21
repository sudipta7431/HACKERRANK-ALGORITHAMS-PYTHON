#!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    # Write your code here
    ll = [0,0]
    for i,j in zip(a,b):
        if i > j:
            ll[0]+=1
        elif i < j:
            ll[1]+=1
        else:
            pass
    return ll
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()