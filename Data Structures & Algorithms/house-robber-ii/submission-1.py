class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def helper(arr):
            dp = [ 0, arr[0] ]

            for i in range(1, len(arr)):
                max_money = max(dp[-1], dp[-2] + arr[i])
                dp.append(max_money)

            return dp[-1]

        return max(helper(nums[1:]), helper(nums[:-1]))
        