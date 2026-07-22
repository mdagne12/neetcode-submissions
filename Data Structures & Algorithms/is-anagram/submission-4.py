class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        for char in s:
            s_freq[char] += 1

        for char in t:
            t_freq[char] += 1

        if len(s_freq) != len(t_freq):
            return False

        for char, count in s_freq.items():
            if t_freq[char] != count:
                return False

        return True
        