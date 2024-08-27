class Solution:
    numOfWays = 0
    def tripleSteps(self,nSteps):
        self.countingSteps(nSteps)
        return self.numOfWays

    def countingSteps(self,nSteps):
        if(nSteps == 0):
            return True
        elif(nSteps < 0):
            return False

        isValidFirstComb = self.countingSteps(nSteps-1)
        isValidSecComb = self.countingSteps(nSteps-2)
        isValidThirdComb = self.countingSteps(nSteps-3)
        if(isValidFirstComb):
            self.numOfWays += 1
        if(isValidSecComb):
            self.numOfWays +=1
        if(isValidThirdComb):
            self.numOfWays += 1


solution = Solution()
result = solution.tripleSteps(7)
print(result)
