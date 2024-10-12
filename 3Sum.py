class Solution:
    def threeSum(nums):
        res = []
        sortedNums = sorted(nums)
        i = 0
        j = 0
        k = len(nums) - 1
        while(i < len(nums) - 1):
            while(0<i<len(nums)-1 and sortedNums[i] == sortedNums[i - 1]):
                i+=1

            j = i + 1
            print('this is sorted',i,j)

            while(j < k):
                print('this is num',j,k)
                total = sortedNums[i] + sortedNums[j] + sortedNums[k]

                if(total == 0):
                    res.append([sortedNums[i],sortedNums[j],sortedNums[k]])
                    j+= 1
                    while(j < k and sortedNums[j] == sortedNums[j-1]):
                        j += 1
                    
                    k -= 1
                    while(k>j and sortedNums[k] == sortedNums[k+1]):
                        k -= 1
                elif(total < 0):
                    j += 1
                    while(j<k and sortedNums[j] == sortedNums[j-1]):
                        j+= 1
                elif(total > 0):
                    k -= 1
                    while(k>j and sortedNums[k] == sortedNums[k+1]):
                        k-= 1

            k = len(nums) - 1
            i += 1

        print(res)
        return res

    threeSum([-1,0,1,2,-1,-4])
