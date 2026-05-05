class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        bestL = bestR = 0

        def expand(l: int, r: int):
            nonlocal bestL, bestR
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > bestR - bestL:
                    bestL, bestR = l, r
                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)       # odd length
            expand(i, i + 1)   # even length

        return s[bestL:bestR + 1]
