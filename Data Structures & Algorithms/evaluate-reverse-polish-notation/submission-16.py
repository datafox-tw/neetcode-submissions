class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            #review: use "isdigit" to find out if it is "positive" number
            #so we can use try-except to try changing str to int
            try:
                i = int(i)
                stack.append(i)
            except:
                print(stack)
                a = stack.pop(-1)
                
                b = stack.pop(-1)
                
                if i=="+":
                    stack.append(b+a)
                if i=="-":
                    stack.append(b-a)
                if i=="*":
                    stack.append(b*a)
                if i=="/":
                    stack.append(int(b/a))
                print(stack)
                print("====")
        return int(stack[-1])
