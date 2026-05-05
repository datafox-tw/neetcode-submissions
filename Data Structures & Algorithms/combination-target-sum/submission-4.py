from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start: int, remain: int):
            if remain == 0:
                res.append(path.copy())
                return

            for i in range(start, len(nums)):
                x = nums[i]
                if x > remain:
                    continue  # 剪枝：後面更大，不可能了

                path.append(x)
                # 這題允許重複選同一個數，所以遞迴仍然用 i（不是 i+1）
                backtrack(i, remain - x)
                path.pop()

        backtrack(0, target)
        return res
