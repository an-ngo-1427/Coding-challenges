class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        usedNum = [0] * len(nums)
        def backtrack(ans,tempList,usedNum,nums):
            if (len(tempList) == len(nums)):
                print(tempList)
                if tempList not in ans:
                    ans.append(tempList[:])
                return

            for i in range(len(nums)):
                if usedNum[i]:
                    continue
                tempList.append(nums[i])
                usedNum[i] = 1
                backtrack(ans,tempList,usedNum,nums)
                tempList.remove(nums[i])
                usedNum[i] = 0

        ans,tempList = [],[]
        backtrack(ans,tempList,usedNum,nums)

        return ans
