class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0


        num_set = set(nums)
        longest_length = 1

        for num in num_set:
            # Only start counting at numbers which are the start of
            # a sequence
            if num - 1 not in num_set:
                curr = num
                curr_len = 1

                while curr + 1 in num_set:
                    curr += 1
                    curr_len += 1

                longest_length = max(longest_length, curr_len)

        return longest_length



        



        