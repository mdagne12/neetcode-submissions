class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Fill s_dict with each char in s and an value representing 
        # how many times the character occurs
        s_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] = s_dict[char] + 1;
            else:
                s_dict[char] = 1

        # Fill s_dict with each char in s and an value representing 
        # how many times the character occurs
        t_dict = {}
        for char in t:
            if char in t_dict:
                t_dict[char] = t_dict[char] + 1;
            else:
                t_dict[char] = 1
        
        if len(s_dict) != len(t_dict):
            return False;
        
        for key in s_dict:
            if key not in t_dict or s_dict[key] != t_dict[key]:
                return False

        return True



        