class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        twoSum = 0

        while left < right:
            twoSum = numbers[left] + numbers[right]

            if twoSum < target:
                left += 1
            elif twoSum > target:
                right -= 1
            else: 
                return [left + 1, right + 1]