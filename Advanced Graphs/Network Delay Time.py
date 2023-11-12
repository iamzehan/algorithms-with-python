import heapq
import collections
class Solution:
    def networkDelayTime (self, times, n, k): 
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges [u].append((v, w))
        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)
            for n2, w2 in edges [n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1

if __name__ == '__main__':
    s = Solution()
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4 # total visited node 
    k = 2 # start node
    print("Output: ", s.networkDelayTime(times, n, k))
