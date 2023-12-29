import heapq
"""
given a list, you have to sort it in two different list, one containing the smaller numbers and the other containing larger numbers

"""
arr = [32, 65, 34, 67, 98, 10, 43, 12, 45, 78, 76, 21, 87, 23, 56, 89, 90, 54]
smaller = []
larger = []

i = 0
j = len(arr)-1

while i<j:
    if arr[i] > arr[j]:
        heapq.heappush(larger, arr[i])
        heapq.heappush(smaller, -arr[j])
    else:
        heapq.heappush(larger, arr[j])
        heapq.heappush(smaller, -arr[i])
        
    if smaller[0]*(-1) > larger[0]:
        l, s  = heapq.heappop(larger)*(-1), heapq.heappop(smaller)*(-1)
        heapq.heappush(smaller, l) 
        heapq.heappush(larger, s)
    
    i+=1
    j-=1

smaller = sorted([i*-1 for i in smaller])
larger = sorted(larger)   
print(smaller, larger)