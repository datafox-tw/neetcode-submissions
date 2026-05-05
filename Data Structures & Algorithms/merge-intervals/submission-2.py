# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         res = []
#         intervals.sort()
#         left = intervals[0][0]
#         right = intervals[0][1]
#         for item in intervals[1:]:
#             print(item)
#             #分三種情況：完全重合，部分重合，完全不重合
#             # 1. 完全重合：直接忽略掉他
#             if left<=item[0] and right>=item[1]:
#                 continue
#             # 2. 部分重合，因為有排序過所以不會有左邊比較大的問題
#             elif left<=item[0]<=right and right<=item[1]:
#                 right = item[1]
#             # 3. 完全不重合，新增處理好的區域到res，換下一個
#             elif right<item[0]:
#                 res.append([left,right])
#                 left = item[0]
#                 right = item[1]
#             print(left,right)
#         if len(res) == 0 or res[-1] != [left,right]:
#             res.append([left,right])
#         return res
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        left, right = intervals[0]

        for s, e in intervals[1:]:
            if s <= right:              # 有重疊（含 touching）
                right = max(right, e)   # 不管包含/部分重疊都吃掉
            else:                       # 完全不重疊
                res.append([left, right])
                left, right = s, e

        res.append([left, right])
        return res
