class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            newnum = 0
            for num in str(n):
                newnum += int(num)**2
            if newnum in seen:
                return False
            elif newnum == 1:
                return True
            else:
                seen.add(newnum)
                n = newnum

