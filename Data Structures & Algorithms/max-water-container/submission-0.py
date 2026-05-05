class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 # 指標一
        right = len(heights) - 1 # 指標二
        max_area = 0 # 最大的面積

        while left < right:

            w = right - left # 算出寬度
            h = min(heights[left], heights[right]) # 算出高度 (從最矮的開始)
            area = w * h # 算出面積
            max_area = max(max_area, area) # 存入最大的面積

            if heights[left] < heights[right]:
                left += 1 # 找下一個比較大的元素
            elif heights[left] > heights[right]:
                right -= 1 # 找前一個比較大的元素
            else:
                # 前後一起縮小
                left += 1
                right -= 1

        return max_area
