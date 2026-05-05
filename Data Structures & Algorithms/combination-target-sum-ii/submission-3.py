class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def backtrack(start: int, remain: int):
            if remain == 0:
                #多一個去重條件：爛方法1
                if path not in res:
                    res.append(path.copy())
                return
            for i in range(start,len(candidates)):
                x = candidates[i]
                if x > remain:
                    break  # 剪枝：後面更大，不可能了
                path.append(x)
                backtrack(i+1, remain-x)
                path.pop()
        backtrack(0, target)
        return res
