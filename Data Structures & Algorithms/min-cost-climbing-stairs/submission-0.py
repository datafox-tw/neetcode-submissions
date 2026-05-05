class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [cost[0], cost[1]]
        for i in range(2,len(cost)):
            mincost.append(min(mincost[-1]+cost[i], mincost[-2]+cost[i]))
        return min(mincost[-1],mincost[-2]) 