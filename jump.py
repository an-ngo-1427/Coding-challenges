class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs (nums,steps,currIndex):
            minSteps = float('inf')
            if(currIndex >= len(nums) - 1):
                return steps
            steps = steps + 1

            for i in range(1,nums[currIndex] + 1):
                pathSteps = dfs(nums,steps,currIndex + i)
                if(pathSteps < minSteps):
                    minSteps = pathSteps
            
            return minSteps
        
        totalSteps = dfs(nums,0,0)
        return totalSteps