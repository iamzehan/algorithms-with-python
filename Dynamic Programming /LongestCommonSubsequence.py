def LongestCommonSubSequence(text1:str, text2:str) -> int:
    dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
    for r in range(len(text1)-1, -1, -1):
        for c in range(len(text2)-1, -1, -1):
            if text1[r] == text2[c]:
                dp[r][c] = dp[r+1][c+1]+1
            else:
                dp[r][c] = max(dp[r][c+1],dp[r+1][c])
    return dp[0][0]

if __name__ == '__main__':
  text1 = "abcde"
  text2 = "ace"
  print(LongestCommonSubSequence(text1, text2))
