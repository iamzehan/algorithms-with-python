s="aab"
def dfs(i,res,part):
    if i>=len(s):
        res.append(part[:])
    for j in range(i,len(s)):
        k = s[i:j+1]
        if k == k[::-1]:
            part.append(s[i:j+1])
            dfs(j+1,res,part)
            part.pop()
    return res
print(dfs(0,[],[])) 
# >>> [['a', 'a', 'b'], ['aa', 'b']]
                
    
