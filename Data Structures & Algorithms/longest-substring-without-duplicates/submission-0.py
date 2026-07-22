class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Stores the frequencies of the characters in our window
        char_freq = defaultdict(int) 
        # Ans will store the length of the longest substring
        left = ans = 0

        for right in range(len(s)):
            char_freq[s[right]] += 1

            while char_freq[s[right]] > 1:
                char_freq[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans

