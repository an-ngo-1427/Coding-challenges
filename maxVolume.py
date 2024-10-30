class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxVolume = 0
        leftIndex = 0
        rightIndex = len(height) - 1

        while(leftIndex < rightIndex):
            width = rightIndex - leftIndex
            leftHeight = height[leftIndex]
            rightHeight = height[rightIndex]

            volume = width * min(leftHeight,rightHeight)
            if(volume > maxVolume):
                maxVolume = volume
            if(rightHeight < leftHeight):
                rightIndex -= 1
            else:
                leftIndex += 1

        return maxVolume
