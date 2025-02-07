class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        num1Dict = {num:1 for num in nums1}
        for num in nums2:
            if num in num1Dict:
                num1Dict[num] -= 1
                if num1Dict[num] == 0:
                    res.append(num)

        return res