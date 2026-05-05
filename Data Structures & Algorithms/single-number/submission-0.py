class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            num = nums[i] ^ nums[i+1]
            nums[i+1] = num
        return  nums[-1]