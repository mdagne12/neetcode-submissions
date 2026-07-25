class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def char_index(char):
            return ord(char) - ord('a')
        
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        if len(s1) > len(s2):
            return False

        # Construct freq_map from the window
        for i in range(len(s1)):
            s1_freq[char_index(s1[i])] += 1
            s2_freq[char_index(s2[i])] += 1

        if s1_freq == s2_freq:
            return True

        for i in range(len(s1), len(s2)):
            # Slide the fixed size window over by 1
            s2_freq[char_index(s2[i])] += 1
            s2_freq[char_index(s2[i - len(s1)])] -= 1

            if s1_freq == s2_freq:
                return True

        return False


