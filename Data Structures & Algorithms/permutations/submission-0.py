class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        # path: 目前已經選了哪些數
        # used: 紀錄哪些 index 已經被用過 (用空間換時間)
        used = [False] * len(nums)

        def backtrack(path):
            # 1. 結束條件：當路徑長度等於 nums 長度，代表找到一組排列
            if len(path) == len(nums):
                res.append(path.copy())
                return

            # 2. 做選擇
            for i in range(len(nums)):
                # 如果這個數字還沒被用過
                if not used[i]:
                    # 做選擇 (加入路徑，標記為已使用)
                    used[i] = True
                    path.append(nums[i])
                    
                    # 進入下一層決策樹
                    backtrack(path)
                    
                    # 3. 回撤 (Backtrack)
                    # 離開下一層後，要取消選擇，恢復狀態
                    path.pop()
                    used[i] = False

        backtrack([])
        return res