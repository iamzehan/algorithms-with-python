import heapq
from collections import Counter, deque
def leastInterval(tasks, n):
	count = Counter(tasks)
	maxHeap = [-cnt for cnt in count.values()]
	heapq.heapify(maxHeap)
	time = 0
	q = deque() #pairs of [-cnt, idleTime]
	while maxHeap or q:
		time += 1
		if maxHeap:
			cnt = 1+heapq.heappop(maxHeap) 
			if cnt:
				q.append([cnt, time + n]) #if count is non-zero, we append it to the queue
		if q and q[0][1] == time: #if current time matches the idleTime of the first item in queue, then we push the count back to our heap. 
			heapq.heappush(maxHeap,q.popleft()[0])
	return time
tasks = ["A","A","A","B","B","B"]
n = 2
print(leastInterval(tasks,n))
>> 8
