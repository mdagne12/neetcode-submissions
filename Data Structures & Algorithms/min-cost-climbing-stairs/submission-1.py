class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # min_cost[i] represents the min cost to reach the step at index i
        dp = [0, 0] 

        for i in range(2, len(cost) + 1):
            dp.append(min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2]))

        return dp[-1]
        