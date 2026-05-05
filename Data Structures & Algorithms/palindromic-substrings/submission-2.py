class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 1
        count = 0
        def expand(l: int, r: int):
            nonlocal count
            while l >= 0 and r < n and s[l] == s[r]:
                # number itself is a palindrone and will add into this part
                # one single number will still fall into this part
                
                count += 1
                l -= 1
                r += 1

        for i in range(n):
            # count += 1
            expand(i, i)       # odd length
            expand(i, i + 1)   # even length

        return count
