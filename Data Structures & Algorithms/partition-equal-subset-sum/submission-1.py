class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # if we evenly partition the array into two subsets with equal sums then 
        # we basically just want to find some subset of elements that add up to 
        # the total sum of all elements divided by two
        target = sum(nums) / 2
        sum_set = {0}

        for num in nums:
            new_sums = []

            for prev_sum in sum_set:
                if prev_sum + num == target:
                    return True
                elif prev_sum + num < target:
                    new_sums.append(prev_sum + num)

            sum_set.update(new_sums)

        return False
