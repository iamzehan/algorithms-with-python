arr = [32, 65, 34, 67, 98, 10, 43, 12, 45, 78, 76, 21, 87, 23, 56, 89, 90, 54]

smaller = []
larger = []

i = 0
j = len(arr)-1

while i<j:
    if arr[i] > arr[j]:
        larger.append(arr[i])
        smaller.append(arr[j])
    else:
        larger.append(arr[j])
        smaller.append(arr[i])
        
    larger = sorted(larger)
    smaller = sorted(smaller)
    
    if smaller[-1] > larger[0]:
        smaller[-1], larger[0] = larger[0], smaller[-1]
    
    i+=1
    j-=1
    
print(smaller, larger) # [10, 12, 21, 23, 32, 34, 43, 45, 54] [56, 65, 67, 76, 78, 87, 89, 90, 98]
