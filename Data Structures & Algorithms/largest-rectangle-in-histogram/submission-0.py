class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #根據不同的底部，去找連續的底
        maxheight = 0
        for idx, h in enumerate(heights):
            #向右延伸，worst case O(N^2)不知道有沒有機會average case O(N)
            right_idx = idx
            left_idx = idx
            while right_idx<len(heights)-1:
                right_idx += 1
                if heights[right_idx] < h:
                    right_idx -= 1
                    break
                
            #向左延伸
            while left_idx > 0:
                left_idx -= 1
                if heights[left_idx] < h:
                    left_idx += 1
                    break
                
            print(h)
            print(left_idx, right_idx)
            maxheight = max(maxheight, h*(right_idx-left_idx+1))
        return maxheight
