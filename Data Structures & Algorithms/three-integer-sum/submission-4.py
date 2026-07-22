class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1
            right = len(nums) - 1

            target = 0 - nums[i]

            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left_num = nums[left]
                    while nums[left] == left_num and left < right:
                        left += 1

                    right_num = nums[right]
                    while nums[right] == right_num and left < right:
                        right -= 1

        return result






        