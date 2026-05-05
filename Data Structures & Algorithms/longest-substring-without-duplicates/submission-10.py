class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # try to use queue, will be faster
        items = []
        maxlength = 0
        for i in s:
            if i in items:
                # if i is a duplicated items, delete all of the characters before the former duplicated letter
                maxlength = max(maxlength, len(items))
                while True:
                    d = items.pop(0)
                    if d == i:
                        break
            # if i is not duplicated items, simply add it to the queue
            items.append(i)
        return max(maxlength, len(items))
