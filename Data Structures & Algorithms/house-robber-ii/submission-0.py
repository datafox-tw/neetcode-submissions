class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            curr = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, curr
        answer1 = curr
        #--------------
        prev2 = nums[1]
        prev1 = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            curr = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, curr
        return max(answer1, curr)
        
