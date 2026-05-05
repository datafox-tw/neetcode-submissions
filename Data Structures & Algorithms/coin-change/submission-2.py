from typing import List
from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None)
        def dp(x: int) -> int:
            if x == 0:
                return 0
            if x < 0:
                return float('inf')  # 不合法路徑，當作無限大

            res = float('inf')
            for c in coins:
                res = min(res, 1 + dp(x - c))

            return res

        ans = dp(amount)
        return -1 if ans == float('inf') else ans
