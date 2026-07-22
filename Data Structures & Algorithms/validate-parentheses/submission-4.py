class Solution:
    def isValid(self, s: str) -> bool:
        matching_chars = {"{":"}", "[":"]", "(":")"}
        stack = []

        for char in s:
            if char in matching_chars:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                
                if matching_chars[stack.pop()] != char:
                    return False

        return len(stack) == 0
