class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevDict = {}

        for i, num in enumerate(nums):
            if target - num in prevDict:
                return [prevDict[target - num], i]
            else:
                prevDict[num] = i
        