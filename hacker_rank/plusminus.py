import math
import os
import random
import re
import sys

def plusMinus(arr):
    # Function to calculate and print the ratio of positive, negative, and zero elements in an array.

    # Calculate the size of the array.
    size = int(len(arr))
    
    # Initialize counters for positive, negative, and zero elements.
    pos_count = 0
    neg_count = 0
    zero_count = 0
    
    # Iterate through each element in the array.
    for num in arr: 
        # Check if the element is positive, negative, or zero, and update counters accordingly.
        if num > 0: 
            pos_count += 1
        elif num == 0: 
            zero_count += 1
        elif num < 0: 
            neg_count += 1
    
    # Print the ratio of positive elements to the total size of the array with 6 decimal places.
    print("{:.6f}".format(float(pos_count / size))); 
    
    # Print the ratio of negative elements to the total size of the array with 6 decimal places.
    print("{:.6f}".format(float(neg_count / size)));
    
    # Print the ratio of zero elements to the total size of the array with 6 decimal places.
    print("{:.6f}".format(float(zero_count / size)));

if __name__ == '__main__':
    # Take input for the size of the array.
    n = int(input().strip())

    # Take input for the elements of the array and convert them to integers.
    arr = list(map(int, input().rstrip().split()))

    # Call the plusMinus function with the array as an argument.
    plusMinus(arr)