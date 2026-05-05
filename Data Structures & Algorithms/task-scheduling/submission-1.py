class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for item in tasks:
            counts[item] = counts.get(item, 0) + 1
        maxFreq = max(counts.values())
        numMax = 0
        for i,j in counts.items():
            if j == maxFreq:
                numMax += 1
        return max( len(tasks), (maxFreq - 1) * (n + 1) + numMax )