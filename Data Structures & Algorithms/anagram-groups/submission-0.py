class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        
        for word in strs:
            frequencies = [0] * 26

            for char in word:
                frequencies[ord(char) - ord("a") ] += 1
            
            if tuple(frequencies) in results:
                results[tuple(frequencies)].append(word)
            else:
                results[tuple(frequencies)] = [word]

        
        return results.values()

        