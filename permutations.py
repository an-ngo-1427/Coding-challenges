class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """ ans,sol = [],[]
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
        return ans """

        def backtrack(ans,tempList,nums):
            if len(tempList) == len(nums):
                ans.append(tempList[:])
                return
            for i in range(len(nums)):
                if nums[i] not in tempList:
                    tempList.add(nums[i])
                backtrack(ans,tempList,nums)
                tempList.pop()

        ans,tempList = [],[]
        backtrack(ans,tempList,nums)

        return ans

    permute([1,2,3])
