class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        nums = sorted(nums)
        longest = 1
        cons = 1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                cons += 1
            elif nums[i+1]-nums[i] == 0:
                continue
            else:
                longest = max(cons, longest)
                cons = 1
        return max(longest, cons)