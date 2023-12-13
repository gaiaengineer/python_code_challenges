# This is basically searching for the biggest sum of a list in a list of lists
# See https://www.geeksforgeeks.org/python-maximum-sum-elements-list-list-lists for future use

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth = 0
        for n in accounts: 
            sum = 0
            for m in n: 
                sum += m
            maxwealth = max(sum, maxwealth)
        return maxwealth
        