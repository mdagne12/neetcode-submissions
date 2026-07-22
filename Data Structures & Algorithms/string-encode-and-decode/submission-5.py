class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + "#" + string 

        return output

    def decode(self, s: str) -> List[str]:

        index = 0
        result = []

        while index < len(s):
            str_len = ""
            while s[index] != '#':
                str_len += s[index]
                index += 1

            str_len = int(str_len)
            index += 1

            result.append(s[index: index + str_len])

            index = index + str_len


        return result


