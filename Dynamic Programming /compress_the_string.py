import pprint
def compress_the_string(string):
    order = ""
    for i in range(len(string)):
        if i == 0 or string[i] != string[i - 1]:
            order += string[i]
    dp = [[0] * (len(string) + 1) for _ in order]
    ans = ""
    visited = set()
    for r in range(len(order)):
        for c in range(1, len(string) + 1):
            if c not in visited and string[c - 1] == order[r]:
                dp[r][c] = dp[r][c - 1] + 1
                visited.add(c)
            elif c not in visited and string[c-1]!=order[r]:
                break
        print(dp[r][c])
        ans += f"{max(dp[r]),int(order[r])} "
    pprint.pprint(dp)
    print("\nOutput: \n",ans.rstrip())
    return ans

if __name__ == '__main__':
    string = "1222311"
    compress_the_string(string)
