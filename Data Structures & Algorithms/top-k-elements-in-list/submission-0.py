class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        # dd_int = defaultdict(int)      # 預設值是 0
        # dd_list = defaultdict(list)    # 預設值是 []
        # dd_set = defaultdict(set)      # 預設值是 set()

        s = defaultdict(int) #initialize every the first entry with 0
        for num in nums:
            s[num] += 1
        # retrieve highest, 用lambda
        s = sorted(s.items(), key = lambda x:x[1])
        final = []
        s.reverse()
        for i in range(k):
            final.append(s[i][0])
        return final