class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        countSet = set()
        res = 0

        for letter in s:
            if letter in countSet:
                countSet.remove(letter)
                res += 2
            else:
                countSet.add(letter)

        if len(countSet):
            return res + 1

        return res
