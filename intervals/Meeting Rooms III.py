import heapq
class Solution(object):
    def mostBooked(self, n, meetings):
        busy = []
        available = [i for i in range(n)]
        
        count = [0]*n
        meetings.sort()
        
        for start, end in meetings:
            while busy and busy[0][0]<=start:
                _end, room = heapq.heappop(busy)
                heapq.heappush(available, room)
                if available:
                    room = heapq.heappop(available)
                    heapq.heappush(busy, (end, room))
                else:
                    time, room = heapq.heappop(busy)
                    heapq.heappush(busy, (time+ end-start, room))
                count[room] += 1
        return count.index(max(count))

if __name__ == '__main__':
    n = 2 
    meetings = [[0,10],[1,5],[2,7],[3,4]]
    s = Solution()
    result = s.mostBooked(n, meetings)
    print(result)
