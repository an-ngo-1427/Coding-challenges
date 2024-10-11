class Solution:

    def insertInterval(intervals,newInterval):
        res = []
        curr_indx = 0
        if not intervals:
            return newInterval

        while curr_indx < len(intervals) and intervals[curr_indx][0] < newInterval[0]:
            res.append(intervals[curr_indx])
            curr_indx += 1
        print('first while')
        if not res or res[-1][1] < newInterval[0]:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1],newInterval[1])

        while curr_indx < len(intervals):
            if(res[-1][1] < intervals[curr_indx][0]):
                res.append(intervals[curr_indx])
            else:
                res[-1][1] = max(res[-1][1],intervals[curr_indx][1])

            curr_indx += 1
        print(res)
        return res

    insertInterval([[1,3],[6,9]],[2,5])
    insertInterval([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])
