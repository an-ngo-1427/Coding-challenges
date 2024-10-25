class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #[0,0,1,1,2,2]
        colorFreq = [0] * 3
        for num in nums:
            colorFreq[num] += 1
        #[2,2,2]
        currIndex = 0
        for freqIndex in range(len(colorFreq)): #2
            for j in range(colorFreq[freqIndex]): #0 - 1
                nums[currIndex] = freqIndex
                currIndex += 1

        return nums
