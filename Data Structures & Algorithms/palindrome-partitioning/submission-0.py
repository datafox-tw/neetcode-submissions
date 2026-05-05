class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []
        n = len(s)
        def backtrack(start):
            if start == n:
                res.append(path.copy())
                return
            for end in range(start, n):
                if is_pal(start, end):
                    path.append(s[start:end+1])
                    backtrack(end+1)
                    path.pop()
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1; r -= 1
            return True
        backtrack(0)
        return res