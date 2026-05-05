class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        cnt = Counter(nums)
        print(cnt)
        return [x for x, _ in heapq.nlargest(k, cnt.items(), key=lambda t: t[1])]
