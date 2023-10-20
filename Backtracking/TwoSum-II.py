def twoSum(nums, target):
    def backtrack(start, target, path):
        if target == 0 and len(path) == 2:
            result.append(list(path))
            return
        if len(path) == 2:
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue  # Skip duplicates to avoid duplicate results
            path.append(i)
            backtrack(i + 1, target - nums[i], path)
            path.pop()

    result = []
    nums.sort()
    backtrack(0, target, [])
    return result

# Example usage:
nums = [1, 2, 2, 3, 4, 5, 5]
target = 7
print(twoSum(nums, target)) # > [[1, 5], [3, 4]]
