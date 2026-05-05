class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        #我想要的寫法是，假設今天有n家可能性，我要讓她recursion到base case但是這題的base case是什麼？
        memo = [-1]*len(nums) #或者是lru cache也可以，或者是先列好一張表 [-1]*n也可以
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]
        x= dfs(0)
        print(memo)
        return x
