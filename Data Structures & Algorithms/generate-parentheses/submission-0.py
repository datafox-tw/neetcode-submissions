class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        countl = 0
        countr = 0
        def backtrack():
            nonlocal countl
            nonlocal countr
            
            if len(path) == n*2:
                result.append("".join(path))
                return
            if countl<n:
                path.append("(")
                countl += 1
                backtrack()
                countl -= 1
                path.pop()
            if countl>countr:
                path.append(")")
                countr += 1
                backtrack()
                countr -= 1
                path.pop()
        backtrack()
        return result
