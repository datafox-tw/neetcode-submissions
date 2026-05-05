class Solution:
    def findMin(self, nums: List[int]) -> int:
        # core thought: the maximum minus the minimum = len(nums)-1
        # core thought 2: when binary search，尋找不是順的那邊，最小值在那裡
        # 如果找不到代表在最左邊
        left = 0
        right = len(nums)-1
        # O(1)
        if nums[right] >= nums[left]:
            return nums[0]
        # O(LOGN)
        while left <= right:
            mid = (right+left) // 2  
            if right - left < 2:
                return min(nums[left], nums[right])
            if nums[mid] > nums[right]:
                #左邊是順的所以解答在右邊
                left = mid
            else:
                #右邊是順的所以解答在左邊
                #兩邊都順：最上面已經處理 nums[0]
                right = mid
        return nums[left]