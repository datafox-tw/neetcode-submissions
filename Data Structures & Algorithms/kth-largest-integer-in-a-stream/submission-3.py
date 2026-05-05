class KthLargest:
    import heapq
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        for n in nums:
            heapq.heappush(self.heap, n)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # 先push再pop即可，不需要一開始先if (self.heap[0]<=val之類的因為一開始可能heap是空的)
        heapq.heappush(self.heap, val) 
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]   # peek，第 k 大
