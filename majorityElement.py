class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countDict = {}

        for num in nums:
            if(num in countDict):
                countDict[num] += 1
            else:
                countDict[num] = 1

        maxCount = max(countDict.values())

        for key in countDict.keys():
            if(countDict[key] == maxCount):
                return key
