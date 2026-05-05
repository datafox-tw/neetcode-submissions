class Solution:
    def myPow(self, x: float, n: int) -> float:
        answer = 1.0
        if n>0:
            for i in range(n):
                answer *= x
        elif n<0:
            for i in range(-n):
                answer *= (1/x)
        return round(answer,5)
