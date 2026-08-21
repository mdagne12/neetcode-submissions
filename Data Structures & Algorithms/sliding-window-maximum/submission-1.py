from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # queue stores indexes not values
        queue = deque()
        l = r = 0
        result = []

        # l = 0, r = 0, result = [], queue = []
        # l = 0, r = 1, result = [], queue = [0]
        # l = 0, r = 2, result = [], queue = [1]
        # 

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            queue.append(r)

            if r >= k - 1:
                result.append(nums[queue[0]])
                l += 1
                if l > queue[0]:
                    queue.popleft()

            r += 1

        return result


            