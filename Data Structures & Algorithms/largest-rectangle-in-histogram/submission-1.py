class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 單調遞增棧：存 index，棧內對應高度遞增
        # 意義：棧中的每根柱子都「還沒遇到右邊第一個更矮的柱子」，所以還有機會往右延伸
        stack = []
        ans = 0

        # 末尾加一根 0，強迫把所有柱子都結算掉
        for i, h in enumerate(heights + [0]):
            
            # 如果當前高度變矮，表示右邊界出現了：開始結算所有比它高的柱子
            while stack and h < heights[stack[-1]]:
                mid = stack.pop()
                height_mid = heights[mid]

                # 左邊界：pop 後的新棧頂是左邊第一個更矮的柱子
                left_smaller = stack[-1] if stack else -1
                width = i - left_smaller - 1

                ans = max(ans, height_mid * width)

            stack.append(i)
            print(stack)

        return ans
