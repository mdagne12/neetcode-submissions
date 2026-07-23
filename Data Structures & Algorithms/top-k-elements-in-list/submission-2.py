class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Create a map of the frequencies of each number
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1

        buckets = [[] for _ in range(len(nums)) ]
        for key, value in num_freq.items():
            buckets[value - 1].append(key)

        print(buckets)
        result = []

        for arr in buckets[::-1]:
            result += arr
            if len(result) == k:
                break

        return result


        
        