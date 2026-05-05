class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        delta = [0]
        for i in range(1, len(temperatures)):
            delta.append(temperatures[i]-temperatures[i-1])
        result = []
        # i know it is O(N^2)
        for index in range(len(delta)):
            num = 0
            count = 0
            flag = False
            for j in delta[index+1:]:
                count +=1
                num += j
                if num>0:
                    result.append(count)
                    flag = True
                    break
            if not flag:
                result.append(0)


        return result