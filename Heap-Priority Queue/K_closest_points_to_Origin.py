import heapq
def kClosest(points, k):
    minHeap = []
    for point in points:
        x, y = point
        distance = (x**2) + (y**2) # for distance from origin, it really doesn't matter that much
        minHeap.append([distance,x,y])
        heapq.heapify(minHeap)
        res = []
    while k>0:
        dist, x, y = heapq.heappop(minHeap)
        res.append([x,y])
        k-=1
    return res
if __name__ == '__main__':
    points = [[0,1],[1,0]]
    k = 2
    print(kClosest(points,k))
