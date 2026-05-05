class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        for r in range(1, len(prices)):
            if prices[r] <prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit
            r += 1
        return max_profit