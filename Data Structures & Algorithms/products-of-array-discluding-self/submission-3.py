class Solution:
    import math
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        if nums.count(0) == 0:
            beichu = math.prod(nums)
            for chu in nums:
                result.append(int(beichu/chu))
        elif nums.count(0) >= 2:
            # should not occur since there is no 0/0
            return [0]*len(nums)
        else:
            beichu = 1
            for i in nums:
                if i != 0:
                    beichu *= i
            for chu in nums:
                if chu != 0:
                    result.append(0)
                else:
                    result.append(int(beichu))

        return result