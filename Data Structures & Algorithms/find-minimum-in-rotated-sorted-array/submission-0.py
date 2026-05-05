class Solution:
    def findMin(self, nums: List[int]) -> int:
        # core thought:the maximum minus the minimum = len(nums)-1
        return min(nums)