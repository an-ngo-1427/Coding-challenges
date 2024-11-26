class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(i,combs,total):
            print('result',total)
            if(total == target):
                result.append(list(combs))
                return
            if(total > target or i >= len(candidates)):
                return

            combs.append(candidates[i])
            dfs(i,combs,total + candidates[i])
            combs.pop()
            dfs(i+1,combs,total)

        dfs(0,[],0)
        return result
    
    def combinationSum1(self,candidates,target):
        result = []
        def dfs(start,combs,target):
            if(target == 0):
                result.append(list(combs))
                return
            for i in range(start,len(candidates)):
                if(candidates[i] > target):
                    continue
                combs.append(candidates[i])
                dfs(i,combs,target - candidates[i])
                combs.pop()
        
        dfs(0,[],target)
        return result