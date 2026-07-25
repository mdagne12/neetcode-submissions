class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height) 
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            # While there's elements on the stack which are taller 
            # than the current height, we pop them off since they 
            # cannot extend any further
            while stack and stack[-1][1] > h:
                prev_i, prev_h = stack.pop()
                max_area = max(max_area, prev_h * (i - prev_i))
                start = prev_i

            stack.append((start, h))

        while stack:
            index, height = stack.pop()
            max_area = max(max_area, height * (len(heights) - index))

        return max_area

