class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        currIndex = 0
        leftIndex = currIndex + 1
        rightIndex = len(nums) - 1
        sumResult = nums[currIndex] + nums[leftIndex] + nums[rightIndex]
        while(currIndex <= len(nums) - 3):
            leftIndex = currIndex + 1
            rightIndex = len(nums) - 1
            while(leftIndex < rightIndex):
                tempSum = nums[currIndex] + nums[leftIndex] + nums[rightIndex]
                if (abs(tempSum - target) < abs(sumResult - target)):
                    sumResult = tempSum
                if(tempSum < target):
                    leftIndex += 1
                elif(tempSum > target):
                    rightIndex -= 1
                else:
                    return tempSum
            currIndex += 1

        return sumResult
