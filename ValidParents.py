class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracketPairsMap = {"[":"]","(":")","{":"}"}
        for i in range(len(s)):
            if(s[i] in bracketPairsMap):
                stack.append(s[i])
            elif(len(stack) and s[i] == bracketPairsMap[stack[-1]]):
                stack.pop()
            else:
                return False

        if(len(stack)):
            return False
        return True
