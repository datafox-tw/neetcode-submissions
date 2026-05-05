class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        combine = []
        # this will tack into effect once the nums are sorted
        def backtrack(start):
            for i in range(start, len(nums)):
                combine.append(nums[i])
                if sum(combine) == target:
                    result.append(combine.copy())
                    print(result)
                    backtrack(i+1)
                if sum(combine)<target:
                    backtrack(i)
                combine.pop()
        backtrack(0)
        return result
