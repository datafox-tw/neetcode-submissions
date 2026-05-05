class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_hour = 1
        max_hour = max(piles)
        import math
        while min_hour <= max_hour:
            mid_hour = min_hour+(max_hour-min_hour)//2
            eating_time = 0
            for i in piles:
                eating_time += math.ceil(i/mid_hour)
            if eating_time > h:
                min_hour = mid_hour+1
            elif eating_time <= h:
                max_hour = mid_hour-1
        return min_hour