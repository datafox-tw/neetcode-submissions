class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        a = ord('a')
        need = [0] * 26
        win = [0] * 26

        for ch in s1:
            need[ord(ch) - a] += 1

        # init window
        for i in range(m):
            win[ord(s2[i]) - a] += 1

        if win == need:
            return True

        # slide
        for r in range(m, n):
            win[ord(s2[r]) - a] += 1
            win[ord(s2[r - m]) - a] -= 1
            if win == need:
                return True

        return False
