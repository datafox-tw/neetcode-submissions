class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #原始狀態：每堂課都沒有先修（尚未建表）
        indegree = [0] * numCourses
        #adj :adjencent每個點的鄰居，代表的是一個投射關係
        adj = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        print(indegree)
        print(adj)
        #我每 pop 出一門課，代表你「已經修掉它」。所以我要先去看哪堂課沒基礎就能修
        q = deque([])
        # 現在的q = 沒有先修條件的課
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        # 我每修一堂課，相對應的進階課先修條件少一，indegree[nxt] -= 1，如果先修修完就可修advance(indegree==0)
        taken  = 0
        while q:
            class_num = q.popleft()
            taken += 1
            for new_class_num in adj[class_num]:
                indegree[new_class_num] -= 1
                if indegree[new_class_num] == 0:
                    q.append(new_class_num)
        #檢查所有課修完時是不是跟numCourses一樣
        return taken == numCourses