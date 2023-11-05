class Solution(object):
	def mergeTriplets(self, tiplets, target):
		good = set()
		for t in triplets:
			if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
				continue
			for i, v in enumerate(t):
				if v == target[i]:
					good.add(i)
		return len(good) == 3
		
if __name__ == '__main__':
    s = Solution()
    triplets = [[2,5,3],[1,8,4],[1,7,5]]
    targets = [[2,7,5],[3,2,5]]
    for target in targets:
        result = s.mergeTriplets(triplets, target)
        print(target, result)
