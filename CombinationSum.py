class Solution:
    def combinationSum(candidates,target):
        sortedCandidates = sorted(candidates)
        tempSum = 0
        comb = []
        ans = []

        for num in sortedCandidates:
            while(tempSum < target):
                tempSum += num
                if(tempSum == target):
                    comb.append(num)
                    ans.append(comb)
                    tempSum = 0
                    comb = []
                    break
                if(tempSum > target):
                    tempSum -= 2*num
                    if(tempSum < 0):
                        return ans
                    comb.pop()
                    break

                comb.append(num)

        print(ans)

    # combinationSum([2,3,6,7],7)
    combinationSum([2,3,5],8)
    # combinationSum([2],1)
