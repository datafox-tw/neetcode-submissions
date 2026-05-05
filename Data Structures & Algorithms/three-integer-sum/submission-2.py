class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_list = []
        nums = sorted(nums)
        for idx, t in enumerate(nums):
            target = -t
            left = idx+1
            right = len(nums)-1
            while left < right: 
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    triplet = [t, nums[left], nums[right]]
                    if triplet not in ans_list:
                        ans_list.append(triplet) 
                    left += 1
                    right -= 1
        return ans_list