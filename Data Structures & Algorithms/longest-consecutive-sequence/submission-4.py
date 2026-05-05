class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        best = 0

        for x in s:
            # 只從序列起點開始
            if x - 1 not in s:
                y = x
                while y in s:
                    y += 1
                best = max(best, y - x)

        return best