class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        money = [nums[0],nums[1]]
        for i in range(2,len(nums)):
            money.append(max(money[-2]+nums[i], money[-1]))
            money[-2] = max(money[0:-1])
        return max(money[-2], money[-1])