class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # try to use queue, will be faster
        if len(s) <=1:
            return len(s)
        items = set(s[0])
        l = 0
        maxlength = 0
        for r in range(1,len(s)):
            if s[r] in items:
                maxlength = max(maxlength, len(items))
                while True:
                    items.remove(s[l])
                    l += 1
                    if s[l-1] == s[r]:
                        break

            items.add(s[r])
        return max(maxlength, len(items))
