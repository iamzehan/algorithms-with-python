class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        start, max_length = 0, 1

        for i in range(n):
            dp[i][i] = 1  # All characters are palindromes of length 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if length == 2 and s[i] == s[j]:
                    dp[i][j] = 2
                elif s[i] == s[j] and dp[i + 1][j - 1] > 0:
                    dp[i][j] = dp[i + 1][j - 1] + 2

                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    start = i

        return s[start:start + max_length]

# Example usage:
solution = Solution()
result = solution.longestPalindrome("babad")
print(result)
