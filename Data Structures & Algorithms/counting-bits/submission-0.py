class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1): #O(N)
            count = 0
            while i: #O(1)
                i &= i-1
                count += 1
            result.append(count)
        return result