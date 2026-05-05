class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        nums = [-i for i in nums] #O(N)
        heapq.heapify(nums) #O(N)
        for _ in range(k): #O(k)
            x = heapq.heappop(nums) #O(logN)
        # overall: max(O(N), O(klogN), 應該是O(N)比較大)
        return -x
