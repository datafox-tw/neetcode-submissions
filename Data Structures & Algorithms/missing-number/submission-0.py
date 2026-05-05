class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1): #O(N)
            nums.append(i)
        ans = 0
        for i in nums:
            ans ^= i
        return ans