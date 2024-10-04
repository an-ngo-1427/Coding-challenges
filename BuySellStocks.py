class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        min = prices[0]
        for i in range(1,len(prices)):
            curr = prices[i]
            if(curr - min > maxProfit):
                maxProfit = curr - min
            if(curr < min):
                min = curr

        return maxProfit
