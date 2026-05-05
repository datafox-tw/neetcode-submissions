class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1) find intersection point
        # 這一步只是在確認「有 cycle」，不是答案。
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        print(slow)
        print(nums[slow])
        #2) find entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
