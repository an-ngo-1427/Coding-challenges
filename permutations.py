class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans,sol = [],[]
        def backtrack():
            if(len(sol) == len(nums)):
                ans.append(sol[:])
                return
            for i in range(len(nums)):
                if(nums[i] not in sol):
                    sol.append(nums[i])
                    backtrack()
                    sol.pop()
        
        backtrack()
        return ans