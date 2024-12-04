class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end,far = 0,0
        smallest = 0
        for i in range(len(nums)-1):
            far = max(far,nums[i] + i)
            if(i == end):
                smallest = smallest + 1
                end = far
        
        return smallest