class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ## loop through the nums array, look for a pivot point that could be swapped to create the next bigger permutation
        ## after swapping, sort the half to the right of the pivot point in ascending order to find the smallest posible combination
        pivot = None
        for i in range(len(nums)-1,0,-1):
            print(i)
            if (nums[i] > nums[i-1]):
                pivot = i-1
                break

        else:
            nums.reverse()
            return

        swap = len(nums)-1
        while(nums[swap] <= nums[pivot]):
            swap -= 1

        nums[pivot],nums[swap] = nums[swap],nums[pivot]
        nums[pivot+1:] = reversed(nums[pivot + 1:])

        return
