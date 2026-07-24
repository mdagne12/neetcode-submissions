class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        freq_map = defaultdict(int)
        left = ans = 0
        
        for right in range(len(s)):
            freq_map[s[right]] += 1

            while freq_map[s[right]] > 1:
                freq_map[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
                

