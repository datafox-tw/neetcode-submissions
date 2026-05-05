class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # method one: sort first and deal with it sequentially.
        while len(stones)>1:
            stones.sort(reverse = True)
            a = stones[0]
            b = stones[1]
            if a-b == 0:
                stones.remove(a)
                stones.remove(b)
            else:
                stones.remove(a)
                stones[0] = abs(a-b)

        if len(stones) == 1:
            return stones[0]
        return 0