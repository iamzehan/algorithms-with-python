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


"""
✅Start:
--------
State:	i=0, res=[[]], sub=[]

Entering Loop:
-------------

range(0,3) - [1, 2, 3]
Appending 1 to sub: [1]

🔄 Recursive Call🔄
---------------

✅Start:
--------
State:	i=1, res=[[], [1]], sub=[1]
Entering Loop:
-------------

range(1,3) - [2, 3]
Appending 2 to sub: [1, 2]

🔄 Recursive Call🔄
---------------

✅Start:
--------
State:	i=2, res=[[], [1], [1, 2]], sub=[1, 2]

Entering Loop:
-------------

range(2,3) - [3]
Appending 3 to sub: [1, 2, 3]

🔄 Recursive Call🔄
---------------

✅Start:
--------
State:	i=3, res=[[], [1], [1, 2], [1, 2, 3]], sub=[1, 2, 3]
🔴Return:	[[], [1], [1, 2], [1, 2, 3]]
🏁End of function call🏁
---------------------
sub=[1, 2, 3]
Popping | 3 | from sub: [1, 2]
🔴Return:	[[], [1], [1, 2], [1, 2, 3]]
🏁End of function call🏁
---------------------
sub=[1, 2]
Popping | 2 | from sub: [1]
range(2,3) - [3]
Appending 3 to sub: [1, 3]

🔄 Recursive Call🔄
---------------

✅Start:
--------
State:	i=3, res=[[], [1], [1, 2], [1, 2, 3], [1, 3]], sub=[1, 3]
🔴Return:	[[], [1], [1, 2], [1, 2, 3], [1, 3]]
🏁End of function call🏁
---------------------
sub=[1, 3]
Popping | 3 | from sub: [1]
🔴Return:	[[], [1], [1, 2], [1, 2, 3], [1, 3]]
🏁End of function call🏁
---------------------
sub=[1]
Popping | 1 | from sub: []
range(1,3) - [2, 3]
Appending 2 to sub: [2]

🔄 Recursive Call🔄
---------------

✅Start:
--------
State:	i=2, res=[[], [1], [1, 2], [1, 2, 3], [1, 3], [2]], sub=[2]

Entering Loop:
-------------

range(2,3) - [3]
Appending 3 to sub: [2, 3]

🔄 Recursive Call🔄
---------------

✅Start:
--------
State:	i=3, res=[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]], sub=[2, 3]
🔴Return:	[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
🏁End of function call🏁
---------------------
sub=[2, 3]
Popping | 3 | from sub: [2]
🔴Return:	[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
🏁End of function call🏁
---------------------
sub=[2]
Popping | 2 | from sub: []
range(2,3) - [3]
Appending 3 to sub: [3]

🔄 Recursive Call🔄
---------------

✅Start:
--------
State:	i=3, res=[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]], sub=[3]
🔴Return:	[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
🏁End of function call🏁
---------------------
sub=[3]
Popping | 3 | from sub: []
🔴Return:	[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
🏁End of function call🏁
---------------------
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
> 
"""
