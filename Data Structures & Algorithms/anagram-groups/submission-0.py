class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using dict
        all_dict = dict()
        final = []
        for idx,vocab in enumerate(strs):
            s_dict = dict()
            for i in vocab:
                if i not in s_dict:
                    s_dict[i] = 0
                s_dict[i] += 1
            s_dict = sorted(s_dict.items(), key=lambda item: item[0])
            if str(s_dict) not in all_dict:
                all_dict[str(s_dict)] = [idx]
            else:
                all_dict[str(s_dict)].append(idx)
        print(all_dict)
        for i in all_dict.values():
            new_ls = []
            for j in i:
                new_ls.append(strs[j])
            final.append(new_ls)
        return final
