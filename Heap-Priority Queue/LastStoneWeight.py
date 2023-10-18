import heapq
def LastStoneWeight(stones):
    """
    :type stones: List[int]
    :rtype: int
    """
    stones = [-stone for stone in stones] #max heap
    heapq.heapify(stones)
    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if second > first:
            heapq.heappush(stones, first-second) #first one is the largest so anyway -8 -(-7) = -1
    stones.append(0)
    return abs(stones[0])
print(LastStoneWeight([3,1]))
print(LastStoneWeight(stones = [2,7,4,1,8,1]))
