class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            new_subsets = []
            for subset in result:
                new_subset = subset.copy()
                new_subset.append(num)
                new_subsets.append(new_subset)

            result.extend(new_subsets)

        return result

