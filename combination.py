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
