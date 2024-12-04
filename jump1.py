class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        targetIndex = len(nums) -1
        for i in range(len(nums)-1,-1,-1):
            if(i+nums[i] >= targetIndex):
                targetIndex = i
            
        if(targetIndex != 0):
            return False
        
        return True