# Longer solution, which takes more memory space and creates an extra array to store results
#class Solution:
    #def runningSum(self, nums: List[int]) -> List[int]:
        #running_sum = [] 
        #for i in range(len(nums)):
            #if i == 0: 
                #running_sum.append(nums[i])
            #else: 
                #running_sum.append(nums[i] + running_sum[i-1])
        #return running_sum

# Optimized solution
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums