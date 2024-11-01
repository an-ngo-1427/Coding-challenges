class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nonValFreq = {}
        kCount = 0
        kIndex = 0
        for num in nums:
            if num == val:
                continue
            if num in nonValFreq:
                nonValFreq[num] += 1
            else:
                nonValFreq[num] = 1
                nums[kIndex] = num
                kIndex += 1
        
        for key,value in nonValFreq.items():
            kCount += value
        
        return kCount