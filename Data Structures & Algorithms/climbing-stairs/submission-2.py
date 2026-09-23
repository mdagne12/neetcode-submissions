class Solution:
    def climbStairs(self, n: int) -> int:
        # memo[i] represents the number of ways you can reach stair i
        memo = { 1:1, 2:2 }
        def dp(i):
            if i in memo:
                return memo[i]

            num_ways_to_reach_i = dp(i - 1) + dp(i - 2)
            memo[i] = num_ways_to_reach_i

            return memo[i]
            
        return dp(n)