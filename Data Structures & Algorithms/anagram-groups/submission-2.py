class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # 一個單字都會有一組res 會是ex. abce = [1,1,1,0,1,0,0,0...] 用這個當key
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
            print(res)
        return list(res.values())
