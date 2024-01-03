#https://www.hackerrank.com/challenges/three-month-preparation-kit-breaking-best-and-worst-records/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as a parameter.
#

def breakingRecords(scores):
    # Initialize variables to keep track of the highest and lowest scores.
    least = scores[0]   # Initialize least with the first element in the scores array.
    most = scores[0]    # Initialize most with the first element in the scores array.
    
    # Initialize counters for the number of times the records are broken.
    count_less = 0      # Counter for the number of times the lowest score is broken.
    count_more = 0      # Counter for the number of times the highest score is broken.
    
    # Iterate through the scores array to find the number of times records are broken.
    for element in scores:
        if element > most:
            count_more += 1  # Increment count_more when a new highest score is encountered.
            most = element   # Update the most variable with the new highest score.
        if element < least:
            count_less += 1  # Increment count_less when a new lowest score is encountered.
            least = element  # Update the least variable with the new lowest score.
    
    # Create an array containing the count of times the highest and lowest records were broken.
    arr = [count_more, count_less]
    
    # Return the result array.
    return arr

if __name__ == '__main__':
    # Open a file for writing the output.
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of elements in the scores array.
    n = int(input().strip())

    # Read the elements of the scores array.
    scores = list(map(int, input().rstrip().split()))

    # Call the breakingRecords function and store the result.
    result = breakingRecords(scores)

    # Write the result array to the output file.
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    # Close the output file.
    fptr.close()
