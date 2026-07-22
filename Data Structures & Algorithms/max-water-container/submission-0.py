class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max_amount = min(heights[left], heights[right]) * (right - left)

        while (left < right):

            curr_amount = min(heights[left], heights[right]) * (right - left)
            if curr_amount > max_amount:
                max_amount = curr_amount

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        
        return max_amount


        