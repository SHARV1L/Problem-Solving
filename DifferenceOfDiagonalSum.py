#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    sum_left = 0
    sum_right = 0
    
    # Approach 1:
    # for i in range(n):
        
    #     sum_left += arr[i][i]
        
    #     sum_right += arr[i][n-i-1]
    
    # Approach 2:
    
    for i in range(n):
        for j in range(n):
            if i == j:
                sum_left += arr[i][j] 
            if i+j == n-1:
                sum_right += arr[i][j]    
              
                
    return (abs(sum_right - sum_left))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
