class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) <= 1:
            return False
        for char in s:
            if char in "[{(":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if (char == "}" and stack[-1] != "{"):
                    return False
                elif (char == ")" and stack[-1] != "(") :
                    return False
                elif (char == "]" and stack[-1] != "["):
                    return False
                else:
                    stack.pop(-1)
        if len(stack) == 0:
            return True  
        else:
            return False
                
