class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_map = {}

        for num in nums:
            if num - 1 in num_map:
                num_map[num] = 1 + num_map[num - 1]
            else:
                num_map[num] = 1

            next_num = num + 1
            while next_num in num_map:
                num_map[next_num] = 1 + num_map[next_num - 1]
                next_num += 1

        max_seq = 0
        for num in num_map.values():
            max_seq = max(max_seq, num)
            
        return max_seq





        
        