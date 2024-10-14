class Solution:
    def productOfArray(nums):

        ans = [0] * len(nums)
        leftProduct = 1
        for i in range(len(nums)):
            if(i == 0):
                ans[i] = leftProduct
            else:
                leftProduct = leftProduct * nums[i-1]
                ans[i] = leftProduct

        rightProduct = 1
        for j in reversed(range(len(nums))):
            ans[j] = ans[j] * rightProduct
            rightProduct = rightProduct * nums[j]

        return ans
    productOfArray([1,2,3,4])
