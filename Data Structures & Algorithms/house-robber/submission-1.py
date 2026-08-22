class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [ 0, nums[0] ]

        for i in range(1, len(nums)):
            max_money = max(dp[-2] + nums[i], dp[-1])
            dp.append(max_money)

        return dp[-1]

        