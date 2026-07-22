class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]

        for i in range(0, len(height) - 1):
            max_left.append(max(max_left[-1], height[i]))

        max_right = [0]

        for i in range(len(height) - 1, 0, -1):
            max_right.insert(0, max(max_right[0], height[i]))

        water_stored = [0] * len(height)
        
        for i in range(len(height)):
            water = min(max_left[i], max_right[i]) - height[i]
            if water > 0:
                water_stored[i] = water

        return sum(water_stored)

        