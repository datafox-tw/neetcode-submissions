from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1) build graph
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        INF = 10**18
        dist = [INF] * (n + 1)
        dist[k] = 0

        # (time_so_far, node)
        heap = [(0, k)]

        while heap:
            t, u = heapq.heappop(heap)
            # stale entry
            if t != dist[u]:
                continue

            for v, w in graph[u]:
                nt = t + w
                if nt < dist[v]:
                    dist[v] = nt
                    heapq.heappush(heap, (nt, v))

        ans = max(dist[1:])  # nodes are 1..n
        return -1 if ans >= INF else ans
