class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = curr_profit = max_profit = 0

        for right in range(len(prices)):
            curr_profit = prices[right] - prices[left]

            while curr_profit < 0 and left < right:
                left += 1
                curr_profit = prices[right] - prices[left]

            max_profit = max(max_profit, curr_profit)
        
        return max_profit
