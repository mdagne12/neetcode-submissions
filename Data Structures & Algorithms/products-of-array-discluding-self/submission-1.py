class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [ 1 ]

        for num in nums[0:-1]:
            prefix.append(prefix[-1] * num)

        suffix = [ 1 ]

        for num in nums[:0:-1]:
            suffix.append(suffix[-1] * num)

        suffix.reverse()

        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])

        return result


        

        