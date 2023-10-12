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
  
  
  """
  TOTAL BREAK DOWN:
  =================
  [1,2,3]
  1 pop
  2 pop
  stack: |1|2|
  main array: |3|
  [[3]] returned
  [[3,2]] ----- 2 appended (LIFO) -- append to main array
  stack: |1|
  main array: |3|2|
  3 pop
  stack: |1|3|
  main array: |2|
  [[2]] returned
  [[2,3]] -----  3 appended (LIFO) -- append to main array
  stack: |1|
  main array: |2|3|
  result: [[3,2],[2,3]] 
  remaining in stack: |1|
  result: [[3,2,1],[2,3,1]] ----- 1 appended to each (LIFO) -> return and hold
  stack: | |
  main array: |2|3|1|
  __________________
  [2,3,1]
  2 pop
  3 pop
  stack: |2|3|
  main array: |1|
  [[1]] returned
  [[1,3]] -----  3 appended (LIFO) -- append to main array
  stack: |2|
  main array: |1|3|
  1 pop
  stack: |2|1|
  main array: |3|
  [[3]] returned
  [[3,1]] ----- 1 appended (LIFO) -- append to main array
  
  stack: |2|
  main array: |3|1|
  result: [[1,3],[3,1]]
  remaining in stack: |2|
  result: [[1, 3, 2], [3, 1, 2]] ----- 2 appended to each (LIFO) -> return and hold
  stack: | |
  main array: |3|1|2|
  ____________________
  [3,1,2]
  3 pop
  1 pop
  stack: |3|1|
  main array: |2|
  [[2]] returned
  [[2,1]] -----  1 appended (LIFO) -- append to main array
  stack: |3|
  main array: |2|1|
  2 pop
  stack: |3|2|
  main array: |1|
  [[1]] returned
  [[1,2]] ----- 2 appended (LIFO) -- append to main array
  stack: |3|
  main array: |1|2|
  result: [[2,1],[1,2]]
  remaining in stack: |3|
  result: [[2, 1, 3], [1, 2, 3]] ----- 3 appended to each (LIFO) -> return and hold
  stack: | |
  
  **** Maximum recursion depth reached: 
  *** Unwind call stacks on hold:
  
  >>> return [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
  """

""" So... this is what's happening 
nums = [1,2,3]
print(permute([1,2,3]))
def permute([1,2,3]):
	result=[]
	len([1,2,3])!=1
	for _ in [1,2,3]:
		#iter 1
		n = [1,2,3].pop(1) >> n = 1 nums = [2,3]
		perms = permute([2,3])
		# recursion 1
			result=[]
			len([2,3])!=1 #ignore
			for _ in [2,3]:
				# iter 1
				n = [2,3].pop(2) >> n = 2, nums = [3]
				perms = permute([3])
					#recursion (1,1)
					result=[]
					len([3])==1:
						return [[3]] >> perms = [[3]] # recursion ends
				for [3] in [[3]]:
					[3].append(2)>> [3,2]
					>> perms = [[3,2]]
				[].extend([[3,2]])>> result = [[3,2]]
				[3].append(2) >> nums = [3,2]
				
				# iter 2
				n = [3,2].pop(3) >> n = 3, nums=[2]
				perms = permute([2])
				# recursion (1,2)
					result = []
					len([2])==1:
						return [[2]] >> perms = [[2]] # recursion ends
				for [2] in [[2]]:
					[2].append(3) >> [2,3]
					>> perms = [[2,3]]
				[[3,2]].extend([[2,3]]) >> result = [[3,2],[2,3]]
				[2].append(3)>> nums = [2,3]
				# for loop ends
			return [[3,2],[2,3]] >> perms = [[3,2],[2,3]] # recursion 1 ends
		for [3,2] and [2,3] in [[3,2],[2,3]]:
			[3,2].append(1) >> [3,2,1] # iter 1
			[2,3].append(1) >> [2,3,1] # iter 2
			>> perms = [[3,2,1],[2,3,1]]
		[].extend([[3,2,1],[2,3,1]]) >> result = [[3,2,1],[2,3,1]]
		[2,3].append(1) >> nums = [2,3,1]

	# iter 2
		n = [2,3,1].pop(2) >> n = 2, nums >> [3,1]
		perms = permute([3,1])
			# recursion 2
			result = []
			len([3,1])!=1 # ignore
			for _ in [3,1]:
				# iter 1
				n = [3,1].pop(3) >> n = 3 >> nums = [1]
				perms = permute([3])
				# recursion 2_1
					result = []
					len([1])==1:
						return [[1]] >> perms = [[1]] # recursion ends
				for [1] in [[1]]:
					[1].append(3) >> [1,3] 
					>> perms = [[1,3]]
				[].extend([[1,3]]) >> result = [[1,3]]
				[1].append(3) >> nums = [1,3]
				# iter 2
				n = [1,3].pop(1) >> n = 1, nums = [3]
				perms = permute([3])
				# recursion 2_2
					result = []
					len([3]) == 1:
						return [[3]] >> perms = [[3]] # recursion ends
				for [3] in [[3]]:
					[3].append(1)
					>> perms = [[3,1]]
				[[1,3]].extend([[3,1]]) >> result = [[1,3],[3,1]]
				[3].append(1) >> nums = [3,1]
				# for loop ends
		for [1,3] and [3,1] in [[1,3],[3,1]]:
			[1,3].append(2) >> [1,3,2]
			[3,1].append(2) >> [3,1,2]
			>> perms = [[1,3,2],[3,1,2]]
		[[3,2,1],[2,3,1]].extend([[1,3,2],[3,1,2]]) 
		>> result = [[3,2,1],[2,3,1],[1,3,2],[3,1,2]]
		[3,1].append(2) >> nums = [3,1,2]

	# iter 3
		n = [3,1,2].pop(2) >> n = 3, nums = [1,2]
		perms = permute([1,2])
		# recursion 3
			result = []
			len([1,2]) != 1  # Continue
			for _ in [1,2]:
			    # Iteration 1
			    n = [1,2].pop(1)  >> n = 1, nums = [2]
			    perms = permute([2])
			    # Recursion (3,1)
			    result = []
			    len([2]) == 1:
			        return [[2]]  # Recursion ends
			    for [2] in [[2]]:
			        [2].append(1)  >> [2,1]
			        >> perms = [[2,1]]
			    [].extend([[2,1]])  >> result = [[2,1]]
			    [2].append(1)  >> nums = [2,1]
			    # Iteration 2
			    n = [2,1].pop(2)  >> n = 2, nums = [1]
			    perms = permute([1])
			    # Recursion (3,2)
			    result = []
			    len([1]) == 1:
			        return [[1]]  >> Recursion ends
			    for [1] in [[1]]:
			        [1].append(2)  >> [1,2]
			        >> perms = [[1,2]]
			    [[2,1]].extend([[1,2]])  >> result = [[2,1],[1,2]]
			    [1].append(2)  >> nums = [1,2]
			    # For loop ends
			return [[2,1],[1,2]]  >> perms = [[2,1],[1,2]]  # Recursion 3 ends
		for [2,1] and [1,2] in [[2,1],[1,2]]:
			[2,1].append(3) >> [2,1,3] #iter 1
			[1,2].append(3) >> [1,2,3] #iter 2
			>> perms [[2,1,3],[1,2,3]]
		[[3,2,1],[2,3,1],[1,3,2],[3,1,2]].extend([[2,1,3],[1,2,3]])
		>> result = [[3,2,1],[2,3,1],[1,3,2],[3,1,2],[2,1,3],[1,2,3]]
		[1,2].append(3) >> nums = [1,2,3]
		# for loop ends
	return [[3,2,1],[2,3,1],[1,3,2],[3,1,2],[2,1,3],[1,2,3]]
"""
