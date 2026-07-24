class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq_map = defaultdict(int)
        left = max_length = 0

        for right in range(len(s)):
            freq_map[s[right]] += 1
            max_freq = max(list(freq_map.values()))

            while right - left + 1 - max_freq > k:
                freq_map[s[left]] -= 1
                left += 1

            max_length = max(right - left + 1, max_length)

        return max_length

