class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        from functools import lru_cache

        @lru_cache(None)
        def dp(i):
            if i == n: #只有一個選擇什麼都不做
                return 1

            elif s[i]=="0":
                # 這個位置不能當一個字母開頭，所以不合法
                return 0
            # take 1 digit
            res = dp(i + 1)

            # take 2 digits if valid (10..26)
            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                res += dp(i + 2)

            return res

        return dp(0)

