class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        def dfs(start,combs,target):
            if(target == 0):
                result.append(list(combs))
                return
            
            for i in range(start,len(candidates)):
                if(i > start and candidates[i] == candidates[i-1]):
                    continue
                if(candidates[i] > target):
                    continue
                combs.append(candidates[i])
                dfs(i+1,combs,target - candidates[i])
                combs.pop()
            

        candidates.sort()
        dfs(0,[],target)
        return result