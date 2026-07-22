class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create two empty dictionaries, one for each word
        # The dictionaries will store all the letters of each word as
        # well as the number of occurrences of each letter
        s_dict = {}
        t_dict = {}

        for char in s:
            # Case for when we've already encountered this letter in the word
            if char in s_dict.keys():
                s_dict[char] = s_dict[char] + 1
            # Case for when we encounter a letter for the first time in the word
            else:
                s_dict[char] = 1

        for char in t:
            if char in t_dict.keys():
                t_dict[char] = t_dict[char] + 1
            else:
                t_dict[char] = 1

        for letter in s_dict:
            if letter not in t_dict or s_dict[letter] != t_dict[letter]:
                return False;

        for letter in t_dict:
            if letter not in s_dict or s_dict[letter] != t_dict[letter]:
                return False;
        
        
        return True;




        