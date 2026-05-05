class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1          # 左移，準備接新 bit
            res |= (n & 1)     # 把 n 的最低位塞進來(和檢查奇數偶數同一招)
            n >>= 1            # n 右移
        return res
