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
if __name__ == '__main__':
  candidates = [10, 1, 2, 7, 6, 1, 5]
  target = 8
  candidates.sort()
  print(backtrack(0, result, [], target))
