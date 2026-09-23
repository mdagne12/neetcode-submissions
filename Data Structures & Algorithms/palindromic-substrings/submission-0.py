class Solution:
    def countSubstrings(self, s: str) -> int:
        # Edge cases: empty string, string with all the came character, 
        # string with all different characters, even length palindromes,
        # odd length palindromes, strings of length one
        n = len(s)
        dp = [ [False] * n for _ in range(n)]
        total_count = 0

        # All strings of length one are palindromes
        for i in range(n):
            dp[i][i] = True
            total_count += 1

        # All strings of length two where the characters are equal are palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                total_count += 1

        # Iterate through all possible substring lengths and starting positions
        # to expand on the previous palindromes identified using dp to avoid 
        # recomputing whether the inner string is a palindrome
        for diff in range(2, n):
            for start in range(n - diff):
                end = start + diff
                if s[start] == s[end] and dp[start + 1][end - 1]:
                    dp[start][end] = True
                    total_count += 1

        return total_count