class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp represents the minimum cost to get to the ith
        # floor 
        dp = [ 0, 0 ]

        for i in range(2, len(cost) + 1):
            curr_cost = min(cost[i - 1] + dp[-1], cost[i - 2] + dp[-2])
            dp.append(curr_cost)

        return dp[-1]

        