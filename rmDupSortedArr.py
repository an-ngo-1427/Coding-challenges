class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        kIndex = 0
        kCount = 1
        for num in nums:
            if(num > nums[kIndex]):
                kIndex += 1
                nums[kIndex] = num
                kCount += 1
        
        return kCount