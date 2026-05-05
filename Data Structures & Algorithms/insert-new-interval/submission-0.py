class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        #i不會重置 從頭用到尾
        # Step 1: 處理在新區間左側且「無重疊」的區間
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        # Step 2: 處理「有重疊」的區間，並合併成一個大的 newInterval
        # 只要現有區間的開始時間 <= newInterval 的結束時間，就代表有重疊
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # 把合併完後的 newInterval 放進去
        res.append(newInterval)
        
        # Step 3: 處理在新區間右側且「無重疊」的區間
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res