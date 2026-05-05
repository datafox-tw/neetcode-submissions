class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        s = defaultdict(int)
        for i in nums:
            s[i] += 1
        s = sorted(s.items(), key = lambda x:x[1])
        s.reverse()
        result = []
        for idx, i in enumerate(s):
            if idx==k:
                break
            result.append(i[0])
        return result