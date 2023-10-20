def SumOfTwo(nums, target):
  num_idx = {}
  for i, n in enumerate(nums):
    complement = target-n
    if complement in num_idx:
      return [num_idx[complement], i]
    else:
      num_idx[n] = i
  return []

if __name__ == '__main__':
  nums, target = [2,7,11,15], 9
  print(SumOfTwo(nums,target))
