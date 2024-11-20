class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.searchBias (nums,target,True)
        right = self.searchBias (nums, target,False)
        return [left,right]
    def searchBias(self,nums,target,leftBias):
        l = 0
        r = len(nums) - 1
        i = -1
        while( l <= r):
            m = (l + r) //2
            if(target < nums[m]):
                r = m -1
            elif(target > nums[m]):
                l = m + 1
            else:
                i = m
                if(leftBias):
                    r = m - 1
                else:
                    l = m + 1

        return i
