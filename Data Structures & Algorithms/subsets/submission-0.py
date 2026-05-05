class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = [] #this will NOT be clear every time, it will contain every possibilities, and result will record them
        def backtrack(start):
            result.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return result
