class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # try to use hashset, is the best
        if len(s) <=1:
            return len(s)
        seen = set(s[0])
        l = 0
        maxlength = 0
        for r in range(1,len(s)):
            if s[r] in seen:
                maxlength = max(maxlength, len(seen))
                while True:
                    seen.remove(s[l])
                    l += 1
                    if s[l-1] == s[r]:
                        break

            seen.add(s[r])
        return max(maxlength, len(seen))
