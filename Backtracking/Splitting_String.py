def splitString(s):
    def dfs(idx, prev):
        if len(s)==idx:
            return True
        for i in range(idx,len(s)):
            val = int(s[idx:i+1])
            print(f"Value: {val}, Previous:{prev}")
            if val==prev-1 and dfs(i+1, val):
                return True
        return False 

    for i in range(len(s)-1):
        val = int(s[:i+1])
        print("Current: ", val)
        if dfs(i+1, val):
            return True
    return False

print(splitString("0090089"))
