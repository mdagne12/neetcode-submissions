class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curr_min, curr_max = 1, 1

        for n in nums:
            saved_curr_max = curr_max
            curr_max = max(n * curr_max, n * curr_min, n)
            curr_min = min(n * saved_curr_max, n * curr_min, n)

            result = max(result, curr_max)

        return result