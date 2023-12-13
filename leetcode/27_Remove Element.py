# My initial solution uses list comprehension https://www.geeksforgeeks.org/remove-all-the-occurrences-of-an-element-from-a-list-in-python
# By doing this, this solution goes against the requirement of modifying the original list in-place (unintentionally)
# And probably is not considered an efficient algo

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [i for i in nums if i != val]
        return len(nums)
    
# This solution is better https://leetcode.com/problems/remove-element/solutions/4013006/two-pointer-in-place-removal-solution/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num_of_nums = 0
        for indx in range(len(nums)):
            if nums[indx] != val:
                nums[num_of_nums] = nums[indx]
                num_of_nums += 1
        return num_of_nums