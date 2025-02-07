class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1Dict = {}
        res= []
        for num in nums1:
            if num in nums1Dict:
                nums1Dict[num] += 1
            else:
                nums1Dict[num] = 1
        
        for num in nums2:
            if num in nums1Dict:
                nums1Dict[num] -= 1
                if nums1Dict[num] >= 0 :
                    res.append(num)

        return res