class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        if len(prices) == 1:
            return 0
        minimum = min(prices[0], prices[1])
        while r < len(prices):
            if prices[r] <prices[l]:
                l = r
                minimum = prices[r]
            else:
                profit = prices[r] - minimum
                if profit > max_profit:
                    max_profit = profit
            r += 1
        return max_profit