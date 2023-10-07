
def dfs(i,combi,total,res):
    if total==target:
        res.append(combi[:])
        return 
    if i>=len(candidates) or total>target:
        return
    combi.append(candidates[i])
    dfs(i,combi,total+candidates[i],res)
    combi.pop()
    dfs(i+1,combi,total,res)
    
    return res

if __name__ == '__main__':
  target=7
  candidates=[2,3,6,7]
  print(dfs(0,[],0,[]))
  # >>> [[2, 2, 3], [7]]
