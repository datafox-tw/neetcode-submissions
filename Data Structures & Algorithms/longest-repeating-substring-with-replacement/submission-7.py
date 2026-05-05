class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        seen = defaultdict(int)
        left = 0
        # O(N)
        all_count = 0
        res = 0
        for right in range(len(s)):
            seen[s[right]] += 1
            all_count += 1
            # 紀錄最多的跟剩下的
            # 剩下的不能夠超過k
            # 超過k的話左側的指標就要往回縮
            max_count = max(seen.values())

            while all_count - max_count > k:
                seen[s[left]] -= 1
                left += 1
                all_count -= 1
                max_count = max(seen.values())
            
            res = max(res, all_count)

        return res