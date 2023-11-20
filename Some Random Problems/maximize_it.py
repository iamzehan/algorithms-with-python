import heapq
def maximize_it(arrays, M, i = 0, li =0, prod =[], maxHeap=[]):
    if len(prod)==len(arrays):
        modulo = -1* (sum(x**2 for x in prod)%M)
        heapq.heappush(maxHeap, modulo)
        return
    for j in range(i,len(arrays[li])):
        prod.append(arrays[li][j])
        maximize_it(arrays, M, i, li+1, prod, maxHeap)
        prod.pop()
    return maxHeap
    
if __name__== '__main__':
    arrays=[
        [2, 5, 4],
        [3, 7, 8, 9],
        [5, 5, 7, 8, 9, 10]
        ]
    M = 1000
    result = maximize_it(arrays, M)[0] * (-1)
    print(result)
