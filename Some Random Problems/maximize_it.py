import heapq
def product(lists, i, li, prod, res, maxHeap=[]):
    if len(prod)==len(lists):
        modulo = -1* (sum(x**2 for x in prod)%1000)
        heapq.heappush(maxHeap, modulo)
        return
    for j in range(i,len(lists[li])):
        prod.append(lists[li][j])
        product(lists,i, li+1, prod, res)
        prod.pop()
    return maxHeap[0]*(-1)
    
if __name__== '__main__':
    lists=[
        [2, 5, 4],
        [3, 7, 8, 9],
        [5, 5, 7, 8, 9, 10]
        ]
    maxModulo=0
    result = product(lists,i=0, li=0, prod=[], res=[])
    print(result)
