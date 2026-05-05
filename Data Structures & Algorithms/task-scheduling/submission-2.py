import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks, n):
        pq = [-c for c in Counter(tasks).values()]
        heapq.heapify(pq)
        time = 0
        cooldown = deque()  # (ready_time, remaining_count)

        while pq or cooldown:
            time += 1

            if pq:
                cnt = heapq.heappop(pq) + 1  # execute once
                if cnt < 0:
                    cooldown.append((time + n, cnt))

            if cooldown and cooldown[0][0] == time:
                heapq.heappush(pq, cooldown.popleft()[1])

        return time
