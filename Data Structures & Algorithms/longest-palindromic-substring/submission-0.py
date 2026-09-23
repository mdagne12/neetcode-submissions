class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] is a boolean value representing whether the substring
        # of s from i to j is a palindrome or not
        n = len(s)
        dp = [ [False] * n for _ in range(n)]
        ans = [0, 0]

        # Every substring of length 1 is technically a palindrome
        for i in range(n):
            dp[i][i] = True

        # Every substring of length 2 where the characters a the 
        # same is a palindrome
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        # Check the longer substrings by expanding the palindromes
        # previously identified, by checking if the left neighbor and 
        # the right neighbor are equal
        for diff in range(2, n):
            for start in range(n - diff):
                end = start + diff

                if dp[start + 1][end - 1] and s[start] == s[end]:
                    dp[start][end] = True
                    ans = [start, end]

        start, end = ans
        return s[start: end + 1]


        