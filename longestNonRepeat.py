class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        uniqueString = set()
        longestLength = 0
        while(right < len(s)):
            if s[right] not in uniqueString:
                uniqueString.add(s[right])
                stringLength = right - left + 1
                if stringLength > longestLength:
                    longestLength = stringLength
                right = right + 1
            else:
                uniqueString.remove(s[left])
                left = left + 1

        return longestLength
