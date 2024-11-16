
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (left + right) //2
            if(nums[mid] == target):
                return mid
            if(target < nums[mid]):
                right = mid -1
            else:
                left = mid + 1
            
       
        if(target < nums[mid] and mid != 0):
            return mid - 1
        elif(target > nums[mid] and mid != 0):
            return mid + 1
        
        return 0