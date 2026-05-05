class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newnums = list(set(nums))
        return (len(newnums) != len(nums))