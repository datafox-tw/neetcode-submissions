class Solution:

    def encode(self, strs: List[str]) -> str:
        newstring = ""
        for s in strs:
            l = len(s)
            newstring += f"{l}#{s}"
        print(newstring)
        return newstring
    def decode(self, s: str) -> List[str]:
        index = 0
        output = []
        while index < len(s):
            for i in range(index,len(s)):
                if s[i] == "#":
                    break
            num = int(s[index:i])
            decoded = s[i+1:i+num+1]
            output.append(decoded)
            index = i+1+num
        return output