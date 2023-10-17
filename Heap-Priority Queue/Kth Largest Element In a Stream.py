import heapq
class KthLargest:
	def __init__(self, k, nums):
		self.minHeap, self.k = nums, k
		heapq.heapify(self.minHeap)
		while len(self.minHeap)>k:
			heapq.heappop(self.minHeap)
	def add(self, val):
		heapq.heappush(self.minHeap, val)
		if len(self.minHeap)>self.k:
			heapq.heappop(self.minHeap)
		return self.minHeap[0] 

param1= ["KthLargest", "add", "add", "add", "add", "add"]
param2 = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
output = []
for i in range(len(param1)):
	if param1[i] == "KthLargest":
		obj = KthLargest(param2[i][0], param2[i][1])
		output.append(None)
	elif param1[i] == "add":
		output.append(obj.add(param2[i][0]))
print(output)
# >> [None, 4, 5, 5, 8, 8]
