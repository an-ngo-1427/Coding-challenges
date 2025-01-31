class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = float('-inf')

        for i in range(len(height) - 1):
            leftSide = height[i]
            for j in range(i+1,len(height)):
                rightSide = height[j]
                currVol = min(leftSide,rightSide) * (j - i)
                if(currVol > maxArea):
                    maxArea = currVol

        return maxArea
