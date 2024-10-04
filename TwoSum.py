class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        valIndPairs ={}
        for i in range(len(nums)):
            val = nums[i]
            if(target - val in valIndPairs):
                return [valIndPairs[target-val],i]

            valIndPairs[val] = i
