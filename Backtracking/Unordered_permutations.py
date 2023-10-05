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
  [[3,2]] ----- 2 added (LIFO)
  stack: |1|
  main array: |3|2|
  3 pop
  stack: |1|3|
  main array: |2|
  [[2]] returned
  [[2,3]] -----  3 added (LIFO)
  stack: |1|
  main array: |2|3|
  result: [[3,2],[2,3]] 
  remaining in stack: |1|
  result: [[3,2,1],[2,3,1]] ----- 1 added to each (LIFO) -> return and hold
  stack: | |
  main array: |2|3|1|
  __________________
  [2,3,1]
  2 pop
  3 pop
  stack: |2|3|
  main array: |1|
  [[1]] returned
  [[1,3]] -----  3 added (LIFO)
  stack: |2|
  main array: |1|3|
  1 pop
  stack: |2|1|
  main array: |3|
  [[3]] returned
  [[3,1]] ----- 1 added (LIFO)
  stack: |2|
  main array: |3|1|
  result: [[1,3],[3,1]]
  remaining in stack: |2|
  result: [[1, 3, 2], [3, 1, 2]] ----- 2 added to each (LIFO) -> return and hold
  stack: | |
  main array: |3|1|2|
  ____________________
  [3,1,2]
  3 pop
  1 pop
  stack: |3|1|
  main array: |2|
  [[2]] returned
  [[2,1]] -----  1 added (LIFO)
  stack: |3|
  main array: |2|1|
  2 pop
  stack: |3|2|
  main array: |1|
  [[1]] returned
  [[1,2]] ----- 2 added (LIFO)
  stack: |3|
  main array: |1|2|
  result: [[2,1],[1,2]]
  remaining in stack: |3|
  result: [[2, 1, 3], [1, 2, 3]] ----- 3 added to each (LIFO) -> return and hold
  stack: | |
  maximum recursion depth
  Unwind call stacks on hold:
  return [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
  """
  
