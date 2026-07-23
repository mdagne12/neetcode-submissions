class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_map = defaultdict(list)

        for word in strs:
            # Store the word in a frequency list each index i corresponds 
            # with the count of the i + 1 th letter of the alphabet

            char_freq = [0] * 26
            for char in word:
                char_freq[ord(char) - ord('a')] += 1

            anagram_map[tuple(char_freq)].append(word)

        return list(anagram_map.values())

        