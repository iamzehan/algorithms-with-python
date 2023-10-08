Here are all the solutions to the Backtracking [Algorithms](Algorithms) problems so far:

* I am going to learn the algorithm's theory in more depth from this [video](https://www.youtube.com/watch?v=DKCbsiDBN6c&ab_channel=AbdulBari)
# Introduction
<iframe width="700" height="350" src="https://www.youtube.com/embed/DKCbsiDBN6c" title="6 Introduction to Backtracking - Brute Force Approach" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
## Permutations I

___
```run-python
def permute(nums):
  result = []
  #base case
  if len(nums) == 1:
    return [nums[:]]
  for _ in nums:
    n = nums.pop(0)
    perms = permute(nums)
    for perm in perms:
      perm.append(n)
    result.extend(perms)
    nums.append(n)
  return result
if __name__ == "__main__":
  nums = [1,2,3]
  print(permute(nums))
```
### Permutations II
___
```run-python
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
```
### Subsets
___
```run-python:
arr=[1,2,3]
def dfs(i, res, subs):
	res.append(subs[:])
	for i in range(i,len(arr)):
		subs.append(arr[i])
		dfs(i+1,res,subs)
		subs.pop()
	return res
print(dfs(0,[],[]))
```
### Splitting a string into Descending Consecutive values
___
```run-python
def splitString(s):
    def dfs(idx, prev):
        if len(s)==idx:
            return True
        for i in range(idx,len(s)):
            val = int(s[idx:i+1])
            if val==prev-1 and dfs(i+1, val):
                return True
        return False 

    for i in range(len(s)-1):
        val = int(s[:i+1])
        if dfs(i+1, val):
            return True
    return False

print(splitString("0090089"))
```
### Word Search
[Problem Link](https://leetcode.com/problems/word-search/)
___
```run-python
def word_search(grid:list[list[str]],word:str)->bool:
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(r, c,0):
                return True
    return False

def explore(r:int, c:int, i:int)->bool:
    if i==len(word):
        return True
    if (
        r < 0 or r >= len(grid) or 
        c < 0 or c >= len(grid[0]) or 
        grid[r][c] != word[i]
        ):
        return False
    
    temp, grid[r][c] = grid[r][c], "*"
    
    if(explore(r-1, c, i+1) or
        explore(r+1, c, i+1) or
        explore(r, c-1, i+1) or
        explore(r, c+1, i+1)):
        return True
    grid[r][c]=temp
    return False
    
    
if __name__ == '__main__':
    #global
    grid = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
    word = "ABCCED"
    
    if not word_search(grid, word):
        print(f"Couldn't find \"{word}\"")
    else:
        print(f"\"{word}\" Found!")
```


### Letter Combinations of a Phone Number

```run-python:
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    digitsToChar = { 
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
        }
    def backtrack(i, res, currStr):
        if len(currStr)==len(digits):
            res.append(currStr)
            return 
        for c in digitsToChar[digits[i]]:
            backtrack(i+1, res, currStr+c)
        return res
    
    if digits:
        return backtrack(0, [], "")
    else:
        return []
print(letterCombinations("23"))
```
### Combination Sum I 
[Problem Link](https://leetcode.com/problems/combination-sum/)
___
```run-python
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

```

### Combination Sum II 
[Problem Link](https://leetcode.com/problems/combination-sum-ii/)
___
```run-python
def backtrack(pos, res, combi, target):
    if target == 0:
        res.append(combi[:])
        return

    for i in range(pos, len(candidates)):
        if candidates[i] > target:
            break  # Skip candidates that are too large, as the list is sorted.

        if i > pos and candidates[i] == candidates[i - 1]:
            continue  # Skip duplicates to avoid duplicate combinations.

        combi.append(candidates[i])
        backtrack(i + 1, res, combi, target - candidates[i])
        combi.pop()
    return res
if __name__ == '__main__':
  candidates = [10, 1, 2, 7, 6, 1, 5]
  target = 8
  candidates.sort()
  print(backtrack(0, [], [], target))
```

### N-Queens Problem

Solution will be available here [Learning](Learning)
___

