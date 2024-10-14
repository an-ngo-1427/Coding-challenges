class Solution:
    def productOfArray(nums):

        ans = [0] * len(nums)
        leftProduct = 1
        for i in range(len(nums)):
            print('leftproducts',leftProduct)
            if(i == 0):
                ans[i] = leftProduct
            else:
                leftProduct = leftProduct * nums[i-1]
                ans[i] = leftProduct

        rightProduct = 1
        for j in reversed(range(len(nums))):
            print('rightproducts',rightProduct)
            ans[j] = ans[j] * rightProduct
            rightProduct = rightProduct * nums[j]

        print(ans)
        return ans
    productOfArray([1,2,3,4])
