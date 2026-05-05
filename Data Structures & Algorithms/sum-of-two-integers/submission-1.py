class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xffffffff
        MAX = 0x7fffffff  # 最大正數（2^31 - 1）

        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # 如果是負數（最高位是 1），轉回 Python 的負數
        return a if a <= MAX else ~(a ^ MASK)
