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
  
