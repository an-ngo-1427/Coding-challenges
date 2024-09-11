class Solution:
    def matrixIndex(self,arr):
        print(self.findIdx(arr,0,len(arr)-1))

    def findIdx(self,arr,highIdx,lowIdx):
        midIdx = highIdx + (lowIdx - highIdx)//2
        if(midIdx == highIdx):
            return -1
        if(midIdx == arr[midIdx]):
            return midIdx
        return self.findIdx(arr,midIdx,lowIdx)


solution = Solution()
solution.matrixIndex([15,10,2,1,0])
solution.matrixIndex([20,18,17,15,14,13,6,2,1])
solution.matrixIndex([20,18,12,1,0])
