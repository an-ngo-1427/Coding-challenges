class Solution:
    def threeSum(nums):
        res = []
        sortedNums = sorted(nums)
        i = 0
        j = 0
        k = len(nums) - 1
        print('this is num',nums)
        while(i < len(nums) - 1):
            print('this is sorted',i)
            j = i + 1

            while(j != k):
                total = sortedNums[i] + sortedNums[j] + sortedNums[k]
                print('total',total)
                if(total == 0):
                    res.append([sortedNums[i],sortedNums[j],sortedNums[k]])
                    break
                elif(total < 0):
                    j += 1
                elif(total > 0):
                    k -= 1

            k = len(nums) - 1
            i += 1

        print(res)
        return res

    threeSum([-1,0,1,2,-1,-4])
