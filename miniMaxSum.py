#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr
    
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr 

def miniMaxSum(arr):
    # Write your code here

    # We'll sort the array into ascending order and then add first four and then last four integers for our    solution. We will test with both selection and bubble sort approaches.
    
    array = selection_sort(arr)
    array = bubble_sort(arr)
    
    
    min_sum = sum(array[:4])
    max_sum = sum(array[1:])
    
    print(min_sum, max_sum)
    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
