class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[(len(nums))//2]
    
# Alternative solution

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set_nums = set(nums)
        for i in set_nums:
            if nums.count(i)>len(nums)/2:
                return i
            

# To solve it in O(N)O(N)O(N) time and O(1)O(1)O(1) space, we can not use a hashmap (O(N)O(N)O(N) space) or sort the array in-place (O(NlogN)O(NlogN)O(NlogN) time). 
# Therefore, we have to use Boyer-Moore’s majority voting algorithm which does the trick.
# https://reintech.io/blog/python-and-the-majorityelement-problem

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        count = 0

        for num in nums:
            if count == 0:
                result = num
            
            if num == result:
                count += 1
            else:
                count -= 1
        
        return result