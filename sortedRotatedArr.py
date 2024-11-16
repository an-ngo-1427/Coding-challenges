class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while(left <= right):
            mid = (left + right) // 2
            print(left,right,mid)
            midVal = nums[mid]

            if(midVal == target):
                return mid
            elif(nums[left] <= midVal):
                if(nums[left]<=target<midVal):
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if(midVal<target<=nums[right]):
                    left = mid + 1
                else:
                    right = mid -1
                
        return -1