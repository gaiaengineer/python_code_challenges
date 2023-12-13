# Import necessary modules
import math
import os
import random
import re
import sys

# Define a function named miniMaxSum that takes a list of integers 'arr' as input
def miniMaxSum(arr):
    # Calculate the minimum and maximum sums of four out of five elements in the array
    # by subtracting each element from the total sum of the array
    # and using generator expressions to find the minimum and maximum values
    min_sum = min(sum(arr) - n for n in arr)
    max_sum = max(sum(arr) - n for n in arr)
    
    # Print the calculated minimum and maximum sums
    print(min_sum, max_sum)

# Entry point of the program
if __name__ == '__main__':
    # Read a space-separated list of integers from the user, convert them to a list of integers
    arr = list(map(int, input().rstrip().split()))
    
    # Call the miniMaxSum function with the provided list of integers as an argument
    miniMaxSum(arr)
