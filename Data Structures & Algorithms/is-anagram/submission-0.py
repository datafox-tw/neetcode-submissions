class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # thought:use dict to maintain the frequency of each character:
        s_dict = dict()
        t_dict = dict()
        for i in s:
            if i not in s_dict.keys():
                s_dict[i] = 0
            s_dict[i] += 1
        for j in t:
            if j not in t_dict.keys():
                t_dict[j] = 0
            t_dict[j] += 1
        return (s_dict == t_dict)