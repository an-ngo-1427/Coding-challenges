class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1

        maxArea = float('-inf')
        while(left< right):
            currArea = min(height[left],height[right]) * (right - left)
            if currArea > maxArea:
                maxArea = currArea

            if height[left] < height[right]:
                left = left + 1
            elif height[left] >= height[right]:
                right = right - 1

        return maxArea
        # maxArea = float('-inf')

        # for i in range(len(height) - 1):
        #     leftSide = height[i]
        #     for j in range(i+1,len(height)):
        #         rightSide = height[j]
        #         currVol = min(leftSide,rightSide) * (j - i)
        #         if(currVol > maxArea):
        #             maxArea = currVol

        # return maxArea
