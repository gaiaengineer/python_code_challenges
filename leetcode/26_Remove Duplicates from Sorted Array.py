class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize a pointer 'j' to keep track of the unique elements
        j = 1
        # Iterate over the array starting from the second element
        for i in range(1, len(nums)):
            # Check if the current element is different from the previous one
            if nums[i] != nums[i - 1]:
                # If different, update the element at position 'j' with the current element
                nums[j] = nums[i]
                # Increment the 'j' pointer to move to the next position for the next unique element
                j += 1

        # 'j' represents the length of the subarray containing unique elements
        return j
    