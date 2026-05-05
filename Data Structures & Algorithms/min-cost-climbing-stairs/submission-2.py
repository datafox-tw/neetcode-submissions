class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom up
        # mincost = [cost[0], cost[1]]
        # for i in range(2,len(cost)):
        #     #紀錄從第三階開始到第n階每階的狀況就算不一定是每一階都需要
        #     mincost.append(min(mincost[-1]+cost[i], mincost[-2]+cost[i]))
        # return min(mincost[-1],mincost[-2])  #最後一步可能是跨一步或者是跨兩步（跳過最後一格的cost)
        # top down:只找需要的然後加上去，然後不代表說他要從最上面開始看，而是也是從基層開始看
        
        # top down限定：lru cache 幫助不要一直算算過的東西
        from functools import lru_cache
        n = len(cost)
        @lru_cache(None)
        def dp(i: int) -> int:
            # min cost to step on i (include cost[i])
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            return cost[i] + min(dp(i - 1), dp(i - 2))

        return min(dp(n - 1), dp(n - 2))
