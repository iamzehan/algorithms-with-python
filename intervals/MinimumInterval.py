import heapq
class Intervals:
    def minInterval(self, intervals, queries):
        intervals.sort()
        minHeap = []
        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]

if __name__ == "__main__":
    i = Intervals()
    intervals = [[1,4],[2,4],[3,6],[4,4]]
    queries = [2,3,4,5]
    min_interval = i.minInterval(intervals, queries)
    print(min_interval)
