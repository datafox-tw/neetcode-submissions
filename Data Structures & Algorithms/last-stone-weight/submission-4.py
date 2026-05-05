class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # method two: heapify(max heap).
        import heapq
        max_heap = []
        for item in stones:
            heapq.heappush(max_heap, -item)
        while len(max_heap)>1:
            a = heapq.heappop(max_heap)
            b = heapq.heappop(max_heap)
            if b>a:
                heapq.heappush(max_heap, a-b)
        if len(max_heap) == 1:
            return -max_heap[0]
        return 0