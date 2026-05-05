class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # since space complexity is O(1), we could only use left and right pointer
        # so we can't use "seen" parameter to store like last problem
        # but this is super easy, just maintain a stable window with len(s1)
        from collections import Counter
        c1 = Counter(s1)
        for i in range(0, len(s2)-len(s1)+1):
            words = s2[i:i+len(s1)]
            if c1 == Counter(words):
                return True
        return False