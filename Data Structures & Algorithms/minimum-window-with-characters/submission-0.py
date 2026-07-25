class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        t_count, window = defaultdict(int), defaultdict(int)

        for char in t:
            t_count[char] += 1

        have, need = 0, len(t_count)
        result, res_len = [-1, -1], float('inf')
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] += 1
            if c in t_count and window[c] == t_count[c]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    result, res_len = [left, right], right - left + 1

                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1

                left += 1

        l, r = result
        return s[l:r + 1] if res_len != float('inf') else ""