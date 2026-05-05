class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            newnum = 0
            for divisor in [1000,100,10,1]:
                quotient = n//divisor
                remainder = n%divisor
                if quotient>0:
                    newnum += quotient ** 2
                n = remainder
            if newnum in seen:
                return False
            elif newnum == 1:
                return True
            else:
                seen.add(newnum)
                n = newnum

