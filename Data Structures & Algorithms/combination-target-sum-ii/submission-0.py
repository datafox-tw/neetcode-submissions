class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def backtrack(start: int, remain: int):
            if remain == 0 and path not in res:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                x = candidates[i]
                if x > remain:
                    break  # 剪枝：後面更大，不可能了

                path.append(x)
                # 這題允許重複選同一個數，所以遞迴仍然用 i（不是 i+1）
                backtrack(i+1, remain - x)
                path.pop()

        backtrack(0, target)
        return res
