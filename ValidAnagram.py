class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freqDict = {}

        for i in range(len(s)):
            if(s[i] in freqDict):
                freqDict[s[i]] += 1
            else:
                freqDict[s[i]] = 1
        for j in range(len(t)):
            if(t[j] not in freqDict):
                return False
            freqDict[t[j]] -= 1

        print(freqDict)
        for value in freqDict.values():
            print(value)
            if(value != 0):
                return False

        return True
