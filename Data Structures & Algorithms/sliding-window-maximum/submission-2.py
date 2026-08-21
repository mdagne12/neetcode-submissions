from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # queue stores indexes not values
        queue = deque()
        l = r = 0
        result = []

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            queue.append(r)

            if queue[0] < r - k + 1:
                queue.popleft()

            if r >= k - 1:
                result.append(nums[queue[0]])
                l += 1

            r += 1

        return result


            