def main(arr):
  res = []
  perm = []
  ans={}
  for i in arr:
      if i not in ans:
          ans[i]=1
      else:
          ans[i]+=1
  def dfs():
      if len(arr)==len(perm):
          res.append(perm[:])
          return 
      for n in ans:
          if ans[n]>0:
              perm.append(n)
              ans[n]-=1
              dfs()
              ans[n]+=1
              perm.pop()
      return res
  res = dfs()
  return res

print(main([1,1,2]))
        
