class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        # i represents the index we are either including or not including
        # curr represents the current elements in our subset and total 
        # represents the total sum of all the elements in our subset
        def dfs(i, curr, total):
            # if adding nums[i] pushes the sum above target then adding anything other
            # elements will lead to a sum that is also greater than target
            if i >= len(nums) or total > target:
                return
            elif total == target:
                result.append(curr.copy())
                return
            
            dfs(i + 1, curr, total)

            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()

        dfs(0, [], 0)
        return result
