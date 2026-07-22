class Solution:
    def rob(self, nums: List[int]) -> int:
        # Tracks the max including the current house and skipping the current house
        dp = [0, nums[0]]

        # dp: 0, 2, 9, 10, 12, 16
        # dp: 0, 1, 1, 4, 4
        for money in nums[1::]:
            curr_max_amount = max(money + dp[-2], dp[-1])
            dp.append(curr_max_amount)

        return dp[-1]
        