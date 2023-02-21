#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    # Write your code here
    for i in range(0,n):
        print(f'{" "*(n-1-i)+"#"*(i+1)}')

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)