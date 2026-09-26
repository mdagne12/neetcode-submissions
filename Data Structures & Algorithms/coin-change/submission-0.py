class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # We want to have 12 cents
        # 1, 6, 7
        # Greedy: 7 + 1 + 1 + 1 + 1 + 1      6 coins to get to 12
        # Optimal: 6 + 6                     2 coint to get to 12

        # Key is the amount to reach and the value is the 
        # minimum number of coins needed to reach that amount
        min_num_coins = { coin:1 for coin in coins }
        min_num_coins[0] = 0

        def find_min_coins(target):
            if target in min_num_coins:
                return min_num_coins[target]

            min_coins = float("inf")

            for coin in coins:
                if target - coin > 0:
                    min_coins = min(find_min_coins(target - coin), min_coins)

            min_coins += 1
            min_num_coins[target] = min_coins
            return min_coins

        min_coins = find_min_coins(amount) 
        return min_coins if min_coins != float('inf') else -1 
            
        # dfs(11)  min_coins = 1 + min(dfs(10), dfs(9), dfs(6))
        # dfs(10)  min_coins = 1 + min(dfs(9), dfs(8), dfs(5))
        # dfs(9)   min_coins = 1 + min(dfs(8), dfs(7), dfs(4)) 
        # dfs(8)   min_coins = 1 + min(dfs(7), dfs(6), dfs(3))
        # dfs(7)   min_coins = 1 + min(dfs(6), dfs(5), dfs(2))
        # dfs(6)   min_coins = 1 + min(dfs(5), dfs(4), dfs(1))

