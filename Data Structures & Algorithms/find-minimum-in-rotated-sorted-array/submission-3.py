class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_val = float('inf')

        while left <= right:
            # If the current window is sorted return the min of the nums
            # we've encountered so far and the leftmost element of our window
            if nums[left] < nums[right]:
                return min(min_val, nums[left])

            mid = (left + right) // 2
            min_val = min(min_val, nums[mid])
            # If mid is part of the left sorted side then we need to go right
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return min_val

        