arr=[1,2,3]
def dfs(i, res, subs):
	res.append(subs[:])
	for i in range(i,len(arr)):
		subs.append(arr[i])
		dfs(i+1,res,subs)
		subs.pop()
	return res
print(dfs(0,[],[]))

#>>> [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
