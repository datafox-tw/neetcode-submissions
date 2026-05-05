class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        for i in range(len(num1)-1,-1,-1):  # 從後到前，加上counter來計算這個答案要乘以多少（1,10,100...)
            inner_ans = 0
            for j in range(len(num2)-1,-1,-1):
                n = int(num1[i])*int(num2[j])
                inner_ans += n*(10**(len(num2)-1-j))
            ans += inner_ans*(10**(len(num1)-1-i))
        ans_str = ""
        # create result: integer to string
        # i think 0*0 is nuisance just do it seperately
        if ans <10:
            return str(ans)
        while ans > 0:
            d = ans % 10
            ans_str = str(d) + ans_str
            ans //= 10
        return ans_str

