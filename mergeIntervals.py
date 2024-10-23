class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        intervals.sort(key=lambda interval:interval[0])
        print(intervals)
        for interval in intervals:
            if(not len(res)):
                res.append(interval)
            elif(interval[0] > res[-1][1]):
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1],interval[1])

        return res
