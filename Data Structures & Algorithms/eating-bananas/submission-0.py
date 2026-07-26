class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        min_speed = max(piles)

        while left <= right:
            # Check if Koko can eat all the bananas in the given
            # timeframe h going at mid speed if not go right and 
            # increase speed, if yes go left and check if there's 
            # other smaller speeds that also work
            mid = (left + right) // 2 
            time = 0

            for i in range(len(piles)):
                # Add the time it would take to eat piles[i]
                time += (piles[i] + mid - 1) // mid   

            print(mid, min_speed, time)
            if time <= h:
                min_speed = min(min_speed, mid)
                right = mid - 1
            else:
                left = mid + 1

        return min_speed

                


