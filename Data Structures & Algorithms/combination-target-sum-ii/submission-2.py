class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def backtrack(start: int, remain: int):
            if remain == 0:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                if candidates[i] == candidates[i-1] and i>start:
                    continue
                x = candidates[i]
                if x > remain:
                    break 

                path.append(x)
                backtrack(i+1, remain - x)
                path.pop()

        backtrack(0, target)
        return res
