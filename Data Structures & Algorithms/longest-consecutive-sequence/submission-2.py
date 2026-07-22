class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        num_map = {}
        curr_length = max_length = 1

        for num in nums:
            num_map[num] = 1

        for num in nums:
            if num - 1 not in num_map:
                curr_length = 1
                i = num
                while i + 1 in num_map:
                    curr_length += 1
                    i += 1
                
                max_length = max(max_length, curr_length)

        return max_length



        
        